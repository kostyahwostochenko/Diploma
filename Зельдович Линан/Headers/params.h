#ifndef __PARAMS__
#define __PARAMS__

#include <cmath>
#include <string>


using namespace std;

    // Поменяй параметры ниже!!!!!
    double z = 15;
    double Le_F = 0.5;
    double Le_X = 1;
    double sigma = 0.15;
    double q = 0.9;
    double R = 0.005;
    double speed_config = -0.07725;
    double speed = -0.05225;//-0.5*pow(z, -0.4);

    string Z_str = "Z = 9, ";
    string Le_F_str = "Le_F = 0.5, ";
    string Le_X_str = "Le_X = 1, ";
    string R_str = "R = 0.005, ";
    string q_str = "q = 0.9, ";
    string sigma_str = "sigma = 0.15";
    string txt_str = ".txt";

    double temp_left = 1;
    double X_left = 0;
    double Y_left = 0;

    double temp_right = sigma;
    double X_right = 0;
    double Y_right = 1;

    double L = 700;
    double T = 25000;

    double dx = 0.1;
    double dt = 0.05;

    double c_parab = dt/(dx*dx);
    double teta = 0.7;

    double place = 0.5;
    double T_config = 20000;

    int scale_x = int(L/dx);
    int scale_t = int(T/dt);
    int scale_t_stab = int(T_config/dt);

    int frames_cnt = 100;
    int cnt = scale_t/frames_cnt;


#endif // !__PARAMS__
