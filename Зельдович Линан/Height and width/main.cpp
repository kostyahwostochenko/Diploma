#include <iostream>
#include <vector>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <omp.h>

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


    string file_name = Le_F_str + Le_X_str + R_str + q_str + sigma_str + txt_str;
    string path = "..\\Data\\Height\\" + file_name;

    ofstream speed_file;
    speed_file.open(path);

    ofstream file;
    file.open(path);

    while (z <= 10){

        load_config(temp, X, Y);

        speed = -0.26*pow(z, -0.54);

        for(int i = 1; i < scale_t_stab + 1; i++){

            calculate_w(w, temp, X, Y, z);
            solver_temp(temp, w, X, teta, dt, dx, temp_left, temp_right, q, R, sigma, speed);
            solver_X(w, X, teta, dt, dx, Le_X, X_left, X_right, R, speed);
            solver_Y(w, Y, teta, dt, dx, Le_F, Y_left, Y_right, speed);
        }

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

        file << max_height << " " << width << " " << z << '\n';
        cout << max_height << " " << width << " " << z << '\n';

        z += 0.1;


    }
    file.close();

    return 0;
}
