#ifndef __SOLVER__
#define __SOLVER__

#include <vector>
#include <iostream>
#include <omp.h>


#include"..\Headers\params.h"

using namespace std;

void solver_temp(vector<double>& temp, const vector<double>& w, const vector<double>& X, const double teta, const double dt, const double dx,
                 const double temp_left, const double temp_right, const double q, const double R, const double sigma, const double speed){

    size_t scale_x = temp.size() - 1;
    double c_parab = dt/(dx*dx);

    vector<double> P(scale_x);
    vector<double> Q(scale_x);

    //P[0] = 0;
    //Q[0] = temp_left;
    P[0] = 1;
    Q[0] = 0;

    for(size_t j = 1; j < scale_x; j++){

        double a = -teta*c_parab;
        double b = -(1 + 2*teta*c_parab);
        double c = -teta*c_parab;
        double d = temp[j] + c_parab*(1-teta)*(temp[j+1] - 2*temp[j] + temp[j-1]) + dt*(1-sigma)*(q*R*X[j] + (1-q)*w[j]) - speed*dt*(temp[j+1]-temp[j-1])/(2*dx);

        P[j] = c/(b - a*P[j-1]);
        Q[j] = (a*Q[j-1] - d)/(b - a*P[j-1]);
    }

    temp[scale_x] = temp_right;

    for(int j = scale_x - 1; j >= 0; j--){
        temp[j] = P[j]*temp[j+1] + Q[j];
    }
}



void solver_X(const vector<double>& w, vector<double>& X, const double teta, const double dt, const double dx,
              const double Le_X, const double X_left, const double X_right, const double R, const double speed){

    size_t scale_x = X.size() - 1;
    double c_parab = dt/(dx*dx);

    vector<double> P(scale_x);
    vector<double> Q(scale_x);

    //P[0] = 0;
    //Q[0] = X_left;
    //P[0] = 1;
    //Q[0] = 0;
    // Когда считаем, что слева радикалов 0
    P[0] = 0;
    Q[0] = 0;

    for(size_t j = 1; j < scale_x; j++){

        double a = -teta*c_parab/Le_X;
        double b = -(1 + 2*teta*c_parab/Le_X);
        double c = -teta*c_parab/Le_X;
        double d = X[j] + c_parab*(1-teta)*(X[j+1] - 2*X[j] + X[j-1])/Le_X + dt*w[j] - dt*R*X[j] - speed*dt*(X[j+1]-X[j-1])/(2*dx);

        P[j] = c/(b - a*P[j-1]);
        Q[j] = (a*Q[j-1] - d)/(b - a*P[j-1]);
    }

    X[scale_x] = X_right;

    for(size_t j = scale_x - 1; j > 0; j--){
        X[j] = P[j]*X[j+1] + Q[j];
    }
}



void solver_Y(const vector<double>& w, vector<double>& Y, const double teta, const double dt, const double dx,
              const double Le_F, const double Y_left, const double Y_right, const double speed){

    size_t scale_x = Y.size() - 1;
    double c_parab = dt/(dx*dx);

    vector<double> P(scale_x);
    vector<double> Q(scale_x);

    //P[0] = 0;
    //Q[0] = Y_left;
    P[0] = 1;
    Q[0] = 0;

    for(size_t j = 1; j < scale_x; j++){

        double a = -teta*c_parab/Le_F;
        double b = -(1 + 2*teta*c_parab/Le_F);
        double c = -teta*c_parab/Le_F;
        double d = Y[j] + c_parab*(1-teta)*(Y[j+1] - 2*Y[j] + Y[j-1])/Le_F - dt*w[j] - speed*dt*(Y[j+1]-Y[j-1])/(2*dx);

        P[j] = c/(b - a*P[j-1]);
        Q[j] = (a*Q[j-1] - d)/(b - a*P[j-1]);
    }

    Y[scale_x] = Y_right;

    for(int j = scale_x - 1; j >= 0; j--){
        Y[j] = P[j]*Y[j+1] + Q[j];
    }
}


void calculate_w(vector<double>& w, const vector<double>& temp, const vector<double>& X, const vector<double>& Y, const double z){
    #pragma omp parallel
    {
        #pragma omp for
        for(size_t j = 0; j < w.size(); j++){
            w[j] = z*z*X[j]*Y[j]*exp(z*(1 - 1/temp[j]));
        }
    }
}

#endif // !__SOLVER__
