/************************************************************
 *  Title       : The Traveling Salesman Problem (TSP)      *
 *  Filename    : tsp.cpp                                   *
 *  Author      : Mark Terwilliger                          *
 *  Description : This program computes the shortest path   *
 *                for a salesman to visit N cities (each    *
 *                one exactly once) and return to the       *
 *                beginning city. The input file format is  *
 *                given by sample input data from TSPLIB,   *
 *                an archive of sample TSP data files at    *
 *                The University of Rice.                   *
 ************************************************************/
#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;

#define MAX_POP_SIZE 1000
#define MAX_CITIES 50

struct City
  {
     int   id;
     double x;
     double y;
  };

class Route
  {
   private:
     int   length;
     int   path[MAX_CITIES];
     double cost;
     double fitness;
  public:
  	 double get_fitness() { return fitness; }
  	 double get_cost()    {  return cost; }  
     void  choose_random(int num_cities);
     void  display_path(City cities[]);
     void  find_cost(City cities[]);
     void  compute_fitness(double optimal_route);
     void  permute(int k, int n, City cities[], int num_cities, double &best_route);
     void  mutate_swap();
     void  mutate_shuffle();
  } ;   

double distance (double x1, double y1, double x2, double y2);
void get_init_pop(int num_cities, int pop_size, Route route[], City cities[], double optimal_route);
void run_ga(int numgen, int pop_size, double &best_route, double optimal_route, Route route[], City cities[]);
double pop_sort(Route route[]);

int main() 
{  
   City cities[MAX_CITIES];
   Route route[MAX_POP_SIZE];
   double best_route;
   double optimal_route;
   int pop_size=500;
   int num_cities;
    
   srand (time(NULL));

   ifstream infile("states.txt");         // the input data file;

   clock_t begintime, endtime;
   float elapsedtime=0;
   srand (time(NULL));

  infile >> num_cities;
  cout << "The number of cities: " << num_cities << endl; // display #cities

   for (int i=0; i < num_cities; i++)     // Read coordinates from data file 
    {
     infile >> cities[i].id;
     infile >> cities[i].x;
     infile >> cities[i].y;
//     cout << "City-" << cities[i].id << " has coordiates of x: "
//          << cities[i].x << " and y: " << cities[i].y << endl;
    }
   infile.close();
   
   begintime =  time(NULL);
   cout << "Exhaustive Search" << endl;
   route[0].choose_random(num_cities);
   route[0].find_cost(cities);
   route[0].display_path(cities);
   cout << "\n\n\n";
   best_route = INFINITY;
   route[0].permute(1,num_cities-1, cities, num_cities, best_route);
   optimal_route = best_route;
   endtime =  time(NULL);
   elapsedtime = endtime - begintime;
   cout << "Elapsed time is : " << elapsedtime << endl;
   cout << "Optimal route is " << optimal_route << endl << endl;

   get_init_pop(num_cities, pop_size, route, cities, optimal_route);

   begintime =  time(NULL);
   run_ga (20, pop_size, best_route, optimal_route, route, cities);
   endtime =  time(NULL);
   elapsedtime = endtime - begintime;
   cout << "GA: Elapsed time is : " << elapsedtime << endl;
   route[0].display_path(cities);
 
   return 0;
}

void Route::display_path(City cities[])
{
 int j;
 cout << "Route is : ";
 for (j=0; j < length; j++)
  cout << cities[path[j]].id << " ";
 cout << "Cost: " << setprecision(1) << fixed << cost << endl;
}

void Route::choose_random(int num_cities)
{
 bool chosen[MAX_CITIES];
 int j,k;
 length = num_cities;
 for (j=0; j < length; j++)
   chosen[j] = false;
 
 for (j=0; j < length; j++)
  {
   do
     k=rand() % length;
   while (chosen[k]);
   chosen[k] = true;
   path[j] = k;
  }
}

void Route::find_cost(City cities[])
{
  cost=0;
  for (int j=0; j < length-1; j++)
    cost += distance (cities[path[j]].x, cities[path[j]].y,
                      cities[path[j+1]].x, cities[path[j+1]].y);
  cost += distance (cities[path[length-1]].x, cities[path[length-1]].y, 
                    cities[path[0]].x, cities[path[0]].y);
//  cout << "Cost: " << cost << endl;
}

void Route::permute (int k, int n, City cities[], int num_cities, double &best_route)
{
  int i, temp;
  if (k==n)
    {
     find_cost(cities);
     if (cost < best_route)
       { 
         best_route = cost;
         display_path(cities);
       }
        
    }
  else
   {
     for (i=k; i<=n; i++)
      {
        temp = path[k];
        path[k] = path[i];
        path[i] = temp;
        permute(k+1, n, cities, num_cities, best_route); 
        temp = path[k];
        path[k] = path[i];
        path[i] = temp;
      }
   }
}
       
void Route::compute_fitness(double optimal_route)
{
    fitness = optimal_route / cost;
}

void get_init_pop(int num_cities, int pop_size, Route route[], City cities[], double optimal_route)
{
 int i;
 for (i=0; i<pop_size; i++)
 {
  route[i].choose_random(num_cities);
  route[i].find_cost(cities);
  route[i].compute_fitness(optimal_route);
//  route[i].display_path();
 }
}

double pop_sort(int pop_size, Route route[])
{
  for (int i=0; i<2*pop_size-1; i++)
    for (int j=i+1; j<2*pop_size; j++)
	if (route[i].get_fitness() < route[j].get_fitness())
	   {
	     Route temp = route[i];
	     route[i] = route[j];
	     route[j] = temp;
	    }
  return (route[0].get_fitness());
}

void Route::mutate_swap()
{
  int x1 = rand() % length;
  int x2 = rand() % length;
  while (x1 == x2)
    x2 = rand() % length;
  int temp = path[x1];
  path[x1] = path[x2];
  path[x2] = temp;
}

void Route::mutate_shuffle()
{
  int temp, x1, x2;
  int size   = 3 + rand() % 6;   // Generates the size of the shuffle string [3..8]
  int start  = rand() % (length - size);  // Generates the left bound of string
  for (int i=0; i < 20; i++)
   {
    x1 = start + rand() % size;    // Swap 20 times the numbers in the string
    x2 = start + rand() % size;
    while (x1 == x2)
      x2 = start + rand() % size;
    temp = path[x1];
    path[x1] = path[x2];
    path[x2] = temp;
   }
}

void run_ga(int numgen, int pop_size, double &best_route, double optimal_route, Route route[], City cities[])
{
  cout << "Gen.  Schedule     Fitness" << endl;
  bool done=false;
  int gen=1;
  while (!done)
   {
     for (int i=0; i < pop_size; i++)        // Make copy of the entire population 
	   route[pop_size+i] = route[i];

     for (int num=pop_size; num < pop_size*2; num++)
	 {
       float p = (RAND_MAX - rand()) / static_cast<double>(RAND_MAX); 
	   if (p > 0.5)
	      route[num].mutate_swap();
	   else
	      route[num].mutate_shuffle();
           route[num].find_cost(cities);
	   route[num].compute_fitness(optimal_route);
	  }
     best_route = pop_sort(pop_size, route);
     cout << setw(4) << gen << setw(12) << setprecision(1) << fixed <<
             route[0].get_cost() << setprecision(4) << setw(10) << best_route << endl;
     if (best_route == optimal_route)
	   done = true; 
     if (gen >= numgen)
	   done = true; 
     gen++;
    }
}
      
double distance (double x1, double y1, double x2, double y2)
{
  return sqrt((y2-y1)*(y2-y1) + (x2-x1)*(x2-x1));
}


