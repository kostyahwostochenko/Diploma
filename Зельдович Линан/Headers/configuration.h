#ifndef __CONFIGURATION__
#define __CONFIGURATION__

#include <vector>
#include <fstream>
#include <string>

#include"solver.h"
#include"params.h"


using namespace std;



void print_vector_in_file(const vector<double>& v, ofstream& file){

    for(size_t j = 0; j < v.size(); j++){
        file << v[j] << " ";
    }
    file << '\n';
}



void make_defaul_config(vector<double>& temp, vector<double>& X, vector<double>& Y, const double temp_left, const double X_left,
                        const double Y_left, const double temp_right, const double X_right, const double Y_right, const double place, const double dx){

    //place это коэффициент от 0 до 1

    size_t scale_x = temp.size() - 1;
    size_t marker = size_t(place*scale_x);

    /*
    for(size_t j = 0; j < marker; j++){
        temp[j] = temp_left;
        Y[j] = Y_left;
    }

    for(size_t j = marker; j < scale_x + 1; j++){
        temp[j] = temp_right;
        Y[j] = Y_right;
    }
    */

    for(size_t j = 0; j < temp.size(); j++){
        Y[j] = 0.5*Y_right*(tanh((dx*j - dx*marker)/Le_F) + 1);
        temp[j] = tanh(dx*j - dx*marker)*0.5*(temp_right - temp_left) + 0.5*(temp_right + temp_left);
        X[j] = exp(-(dx*j - dx*marker)*(dx*j - dx*marker)/2) - exp(-dx*marker*dx*marker/2);
    }

    X[0] = X_left;
    Y[0] = Y_left;
    temp[0] = temp_left;

    X[scale_x] = X_right;
    Y[scale_x] = Y_right;
    temp[scale_x] = temp_right;

    remove("..\\Data\\Config\\Params.txt");

    ofstream temp_config;
    temp_config.open("..\\Data\\Config\\Temp.txt");

    ofstream X_config;
    X_config.open("..\\Data\\Config\\X.txt");

    ofstream Y_config;
    Y_config.open("..\\Data\\Config\\Y.txt");

    print_vector_in_file(temp, temp_config);
    print_vector_in_file(X, X_config);
    print_vector_in_file(Y, Y_config);

    temp_config.close();
    X_config.close();
    Y_config.close();
}



void make_config(vector<double>& temp, vector<double>& X, vector<double>& Y, const double temp_left, const double X_left, const double Y_left,
                 const double temp_right, const double X_right, const double Y_right, const double z, const double sigma, const double Le_X,
                 const double Le_F, const double q, const double R, const double teta, const double dt, const double dx, const double T_config, const double place, const double speed){

    int scale_t = int(T_config/dt);
    vector<double> w(temp.size());

    make_defaul_config(temp, X, Y, temp_left, X_left, Y_left, temp_right, X_right, Y_right, place, dx);

    for(int i = 1; i < scale_t + 1; i++){

        calculate_w(w, temp, X, Y, z);
        solver_temp(temp, w, X, teta, dt, dx, temp_left, temp_right, q, R, sigma, speed);
        solver_X(w, X, teta, dt, dx, Le_X, X_left, X_right, R, speed);
        solver_Y(w, Y, teta, dt, dx, Le_F, Y_left, Y_right, speed);

    }


    string path_temp = "..\\Data\\Config\\Temp.txt";
    string path_X = "..\\Data\\Config\\X.txt";
    string path_Y = "..\\Data\\Config\\Y.txt";
    string path_params = "..\\Data\\Config\\Params.txt";

    ofstream Temp_config;
    Temp_config.open(path_temp);

    ofstream X_config;
    X_config.open(path_X);

    ofstream Y_config;
    Y_config.open(path_Y);

    ofstream Params_config;
    Params_config.open(path_params);

    print_vector_in_file(temp, Temp_config);
    print_vector_in_file(X, X_config);
    print_vector_in_file(Y, Y_config);

    Params_config << z << " " << Le_F << " " << Le_X << " " << R << " " << q << " " << sigma << " " << T_config << '\n';

    Temp_config.close();
    X_config.close();
    Y_config.close();
    Params_config.close();

}



void load_config(vector<double>& temp, vector<double>& X, vector<double>& Y){

    ifstream temp_config;
    temp_config.open("..\\Data\\Config\\Temp.txt", ios::in);

    ifstream X_config;
    X_config.open("..\\Data\\Config\\X.txt", ios::in);

    ifstream Y_config;
    Y_config.open("..\\Data\\Config\\Y.txt", ios::in);

    for(size_t j = 0; j < temp.size(); j++){
        temp_config >> temp[j];
        X_config >> X[j];
        Y_config >> Y[j];
    }

    temp_config.close();
    X_config.close();
    Y_config.close();
}




#endif // !__CONFIGURATION__
