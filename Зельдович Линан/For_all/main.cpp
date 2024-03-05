#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <algorithm>

#include"..\Headers\solver.h"
#include"..\Headers\configuration.h"
#include"..\Headers\params.h"

using namespace std;



int main()
{

    vector<double> temp(scale_x + 1);
    vector<double> X(scale_x + 1);
    vector<double> Y(scale_x + 1);
    vector<double> w(scale_x + 1);

    if(cnt < 1){
        cnt = 1;}

    //make_config(temp, X, Y, temp_left, X_left, Y_left, temp_right, X_right, Y_right, z, sigma, Le_X, Le_F, q, R, teta, dt, dx, T_config, place, speed_config);
    make_defaul_config(temp, X, Y, temp_left, X_left, Y_left, temp_right, X_right, Y_right, place, dx);

    string file_name = Z_str + Le_F_str + R_str + q_str + sigma_str + txt_str;
    string path_temp = "..\\Data\\Temperature\\" + file_name;


    ofstream file_temp;
    file_temp.open(path_temp);

    z = 5;

    T_config = 15000;
    dt = 0.05;
    scale_t_stab = int(T_config/dt);

    while (z <= 15.01){

        load_config(temp, X, Y);

        speed_config = -0.29*pow(z, -0.59);

        if(z > 10){
            T_config = 20000;
            scale_t_stab = int(T_config/dt);
        }


        for(int i = 1; i < scale_t_stab + 1; i++){
            calculate_w(w, temp, X, Y, z);

            #pragma omp parallel sections
            {
                #pragma omp section
                solver_temp(temp, w, X, teta, dt, dx, temp_left, temp_right, q, R, sigma, speed_config);

                #pragma omp section
                solver_X(w, X, teta, dt, dx, Le_X, X_left, X_right, R, speed_config);

                #pragma omp section
                solver_Y(w, Y, teta, dt, dx, Le_F, Y_left, Y_right, speed_config);
            }
        }


        auto aaa = distance(X.begin(), max_element(X.begin(), X.end()));

        file_temp << temp[aaa] << " " << z << '\n';
        cout << temp[aaa] << " " << z << '\n';
        cout << '\n';

        z += 0.4;

    }

    file_temp.close();

    return 0;
}
