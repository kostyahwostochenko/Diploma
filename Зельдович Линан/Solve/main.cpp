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

    //make_config(temp, X, Y, temp_left, X_left, Y_left, temp_right, X_right, Y_right, z, sigma, Le_X, Le_F, q, R, teta, dt, dx, T_config, place, speed);
    make_defaul_config(temp, X, Y, temp_left, X_left, Y_left, temp_right, X_right, Y_right, place, dx);
    load_config(temp, X, Y);
    calculate_w(w, temp, X, Y, z);


    string file_name = Z_str + Le_F_str + Le_X_str + R_str + q_str + sigma_str + txt_str;
    string path_Temp = "..\\Data\\Current\\Temp " + file_name;
    string path_X = "..\\Data\\Current\\X " + file_name;
    string path_Y = "..\\Data\\Current\\Y " + file_name;
    string path_W = "..\\Data\\Current\\W " + file_name;

    ofstream temp_file;
    temp_file.open(path_Temp);

    ofstream X_file;
    X_file.open(path_X);

    ofstream Y_file;
    Y_file.open(path_Y);

    ofstream w_file;
    w_file.open(path_W);


    print_vector_in_file(temp, temp_file);
    print_vector_in_file(X, X_file);
    print_vector_in_file(Y, Y_file);
    print_vector_in_file(w, w_file);



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


        if(i%cnt == 0){
            print_vector_in_file(temp, temp_file);
            print_vector_in_file(X, X_file);
            print_vector_in_file(Y, Y_file);
            print_vector_in_file(w, w_file);
            cout << double(i)/scale_t*100 << "%" << '\n';
        }

    }

    temp_file.close();
    X_file.close();
    Y_file.close();
    w_file.close();


    ofstream gif_file;
    gif_file.open("..\\Data\\Current\\Gif.txt");
    gif_file << L << " " << dx << " " << frames_cnt <<'\n';
    gif_file.close();

    ofstream params_file;
    params_file.open("..\\Data\\Current\\Params.txt");
    params_file << z << " " << Le_F << " " << Le_X << " " << R << " " << q << " " << sigma << '\n';
    params_file.close();


    return 0;
}
