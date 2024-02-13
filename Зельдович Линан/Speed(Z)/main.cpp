#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <string>

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
    //make_defaul_config(temp, X, Y, temp_left, X_left, Y_left, temp_right, X_right, Y_right, place, dx);
    //remove("..\\Data\\Speed\\Z\\" + file_name);
    //speed_file.open(path, ios::app);

    string file_name = Le_F_str + Le_X_str + R_str + q_str + sigma_str + txt_str;
    string path = "..\\Data\\Speed\\Z\\" + file_name;

    ofstream speed_file;
    speed_file.open(path);



    while (z <= 10){

        load_config(temp, X, Y);

        for(int i = 1; i < scale_t_stab + 1; i++){
            calculate_w(w, temp, X, Y, z);
            solver_temp(temp, w, X, teta, dt, dx, temp_left, temp_right, q, R, sigma, speed);
            solver_X(w, X, teta, dt, dx, Le_X, X_left, X_right, R, speed);
            solver_Y(w, Y, teta, dt, dx, Le_F, Y_left, Y_right, speed);
        }

        auto max_x_start = max_element(X.begin(), X.end());

        for(int i = 1; i < scale_t + 1; i++){
            calculate_w(w, temp, X, Y, z);
            solver_temp(temp, w, X, teta, dt, dx, temp_left, temp_right, q, R, sigma, speed);
            solver_X(w, X, teta, dt, dx, Le_X, X_left, X_right, R, speed);
            solver_Y(w, Y, teta, dt, dx, Le_F, Y_left, Y_right, speed);
        }

        auto max_x_finish = max_element(X.begin(), X.end());
        double u_speed = distance(max_x_start, max_x_finish)*dx/T;

        speed_file << u_speed << " " << z << '\n';
        cout << u_speed << " " << z << '\n';

        z += 0.1;
    }

    speed_file.close();

    return 0;
}
