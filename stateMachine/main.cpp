#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include "order.hpp"

int main(void)
{
  /* char chr = 'a'; //This will loop until q is pressed on the terminal
  /do {
    int num = getc(stdin);
    chr = (char) num;
  */
    //add code to connect to website here. As request comes in, add to queue
    
    //Struct for the order, add fields as necessary
    Order order;
    OrderData* data = new OrderData();
    data->PID = 100; //Ex. PID
    
    //fork into different processes here
    int cpid = fork();
    if (cpid == 0) {
      order.startOrder(data);
      //} 
    //while(chr != 'q');
    }
  return 0;
}

