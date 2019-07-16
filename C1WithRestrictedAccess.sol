// James Ericsson
// Student Researcher Columbus State Univesrity
// 12 July 2019

// Will be used to append sensor data on to the ethereum testnet Ropsten.
// Would also work on current ethereum main chain.
pragma solidity >=0.4.22 <0.7.0; // More specifically this contract was written during solidity 0.5.10
contract SensorContract {
  // Variables declared outside of functions act as global variables.
  int public sensorCount;
  int[] falseDataArray;
  address owner;
  address privlegedUser;

  // This structure defines an outline for sensor data that will be
  // collected for this experiment.
  struct Sensor {
    int id; // An id for the sensor, it will also act as a key for a mapping used later.
    int max; // A maximum normal temperature.
    int min; // A minimum normal temperature.
    string description; // A description of the sensor, where it is, what it does, etc.
    int abnormalBehaviors; // Variable starts at 0 and will be incremented whenever abnormal behavior is detected
    int[] dataArray;  // An array to store the sensors data.
                      // If we were collected non numeric data this would also work with a bytes32[] array.
  }
  // This mapping will be used for interacting with our sensors.
  // As stated above the key will be the id which is assigned
  // When the sensor is added.
  mapping(int => Sensor) public sensors;


  // When a contract is created it's constructor is executed once.
  // It's optional and only one is allowed. No overloading supported.
  constructor() public{
    addSensor(55, 45, "Contract One, Max:55, Min:45, Standard Array Appendment");
    owner = msg.sender;
    falseDataArray.push(0);
  }


  // If you want it to return something you place it into the unction header in this way.
  // In the paramters you'll notice that after string there is a keyword memory.
  // I can't find any clear reason it's required but the Remix Etheruem IDE doesn't compile without it.
  function addSensor(int max, int min, string memory description) public returns (bool){
    if(msg.sender == owner || msg.sender == privlegedUser){
      sensorCount ++; // There will be no sensor at posistion 0. Upon creation of the first sensor the count should now be 1.
      sensors[sensorCount].id = sensorCount;
      sensors[sensorCount].max = max;
      sensors[sensorCount].min = min;
      sensors[sensorCount].description = description;
      return true;
    }
    else{
      return false;
    }
  }

  function addPrivlegedUser(address newPrivlegedUser) public {
    if (msg.sender != owner) return;
    privlegedUser = newPrivlegedUser;
  }

  // Returns the description for the sensor.
  // Once again string needs to have the memory keyword or it will fail to compile.
  function getDescriptionById(int id) public view returns (string memory) {
    return sensors[id].description ;
  }
  // Apparently arrays also want the memory keyword.
  // Can't seem to just return the entire array...
  function getSensorDataById(int id) public view returns (int[] memory) {
      if(msg.sender == owner || msg.sender == privlegedUser){
        return sensors[id].dataArray;
      }
      else{
        return falseDataArray;
      }
   // return dataArray2;
  }
  //function getSensorDataByIdLength(int id) public returns(uint length){
   // return sensors[id].dataArray.length;
 // }
  // Returns the number of abnormal data reading by the specified sesnor.
  function getAbnormalBehaviorCountById(int id) public view returns(int){
    return sensors[id].abnormalBehaviors;
  }

  // Function adds data to the Sensor data[]
  // Returns a boolean value of true if the data is abnormal.
  // Also increments abnormalBehaviors counter inside of the sensors struct.

  function setDataToSensorById(int id, int data) public returns (bool){
      // Just ignore the compilation warning. It's becasue i didn't need to specify a sensors variable.
      if(msg.sender == owner || msg.sender == privlegedUser){
        Sensor storage sensors = sensors[id];
        // Either condition is considered an abornamal behavior.
        if(data >= sensors.max || data <= sensors.min){
          sensors.abnormalBehaviors ++;
          sensors.dataArray.push(data);
          return true;
        }
        else{
          sensors.dataArray.push(data);
          return false;
        }
      }
  }
}
