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
    //make_defaul_config(temp, X, Y, temp_left, X_left, Y_left, temp_right, X_right, Y_right, place, dx);


    string file_name = Z_str + Le_X_str + R_str + q_str + sigma_str + txt_str;
    string path_speed = "..\\Data\\Speed\\Le_F\\" + file_name;
    string path_height = "..\\Data\\Height\\" + file_name;


    ofstream speed_file;
    speed_file.open(path_speed);

    ofstream file_height;
    file_height.open(path_height);



    Le_F = 2;
    T_config = 20000;
    T = 1000;

    while (Le_F >= 0.49){

        load_config(temp, X, Y);

        speed_config = -0.25*pow(Le_X, -0.16)*pow(z, -0.54);
        dt = 0.1;
        scale_t_stab = int(T_config/dt);

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

        speed = 0;
        dt = 0.02;
        scale_t = int(T/dt);

        auto max_x_start = max_element(X.begin(), X.end());

        for(int i = 1; i < scale_t + 1; i++){
            calculate_w(w, temp, X, Y, z);

            #pragma omp parallel sections
            {
                #pragma omp section
                solver_temp(temp, w, X, teta, dt, dx, temp_left, temp_right, q, R, sigma, speed);

                #pragma omp section
                solver_X(w, X, teta, dt, dx, Le_X, X_left, X_right, R, speed);

                #pragma omp section
                solver_Y(w, Y, teta, dt, dx, Le_F, Y_left, Y_right, speed);
            }
        }

        auto max_x_finish = max_element(X.begin(), X.end());
        double u_speed = distance(max_x_start, max_x_finish)*dx/T;

        speed_file << u_speed << " " << Le_F << '\n';
        cout << u_speed << " " << Le_F << '\n';



        auto itt_max = max_element(X.begin(), X.end());
        auto right_border = itt_max;
        auto left_border = itt_max;

        double max_height = *itt_max;
        double width = -1;

        for(auto itt = itt_max; itt < X.end(); itt++){
            if(abs(max_height/2 - *itt) < abs(max_height/2 - *right_border)){
                right_border = itt;
            }
        }

        for(auto itt = itt_max; itt > X.begin(); itt--){
            if(abs(max_height/2 - *itt) < abs(max_height/2 - *left_border)){
                left_border = itt;
            }
        }

        width = distance(left_border, right_border)*dx;

        file_height << max_height << " " << width << " " << Le_F << '\n';
        cout << max_height << " " << width << " " << Le_F << '\n';
        cout << '\n';


        Le_F -= 0.1;

    }
    speed_file.close();
    file_height.close();

    return 0;
}
