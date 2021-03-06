#ifndef _ORDER_H
#define _ORDER_H
#include "stateMachine.hpp"
#include <string>

using namespace std;

// structure to hold event data passed into state machine
struct OrderData : public EventData
{
  int PID;
  int shippingID;
  string desc;
  int addressX;
  int addressY;
  int quant;
  int WH;
};


// the Order state machine class
class Order : public StateMachine
{
public:
  Order() : StateMachine(ST_MAX_STATES) {}

  // external events taken by this state machine
  void startOrder(OrderData*);

private:
    // state machine state functions
  void ST_Idle(EventData*);  
  void ST_WHPurchase(OrderData*);
  void ST_WHArrived(OrderData*);
  void ST_UPSShip(OrderData*);
  void ST_UPSResp(OrderData*);

  void ST_WHtoPack(OrderData*);
  void ST_WHReady(OrderData*); //Need both events
  void ST_WHLoad(OrderData*);

  void ST_WHLoaded(OrderData*);
  void ST_UPSDeliver(OrderData*);

    // state map to define state function order
  BEGIN_STATE_MAP
  STATE_MAP_ENTRY(&Order::ST_Idle)
  STATE_MAP_ENTRY(&Order::ST_WHPurchase)
    STATE_MAP_ENTRY(&Order::ST_WHArrived)
    STATE_MAP_ENTRY(&Order::ST_UPSShip)
    STATE_MAP_ENTRY(&Order::ST_UPSResp)
    STATE_MAP_ENTRY(&Order::ST_WHtoPack)
    STATE_MAP_ENTRY(&Order::ST_WHReady)
    STATE_MAP_ENTRY(&Order::ST_WHLoad)
    STATE_MAP_ENTRY(&Order::ST_WHLoaded)
    STATE_MAP_ENTRY(&Order::ST_UPSDeliver)
    END_STATE_MAP
    
  // state enumeration order must match the order of state
  // method entries in the state map
    enum E_States { 
    ST_IDLE = 0,
    ST_WHPURCHASE,
    ST_WHARRIVED,
    ST_UPSSHIP,
    ST_UPSRESP,
    ST_WHTOPACK,
    ST_WHREADY,
    ST_WHLOAD,
    ST_WHLOADED,
    ST_UPSDELIVER,
    ST_MAX_STATES
  };
};
#endif // _ORDER_H
