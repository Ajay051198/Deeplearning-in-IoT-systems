## Deeplearning-in-IoT-systems
### *Master's Project @University of British Columbia*
---
### Objective of Project: 

- **Analysis**: Evaluation of the current state of the art of IoT architecture and Deep Learning systems followed by an
analysis of the use of Deep Learning and IoT technologies in union to improve existing IoT architecture
- **Implementation**: Demonstration of the proposed idea by applying sequence analysis using RNN’s on temporal
time series sensor data to perform human activity recognition to assist smart home system to adapt to the dynamic
environment and deal with noise better

---

### Dataset: 
[CASAS Dataset] http://casas.wsu.edu/datasets/

--- 
### Data Preprocessing

**DATA**

<img src="./assets/data.png"
     alt="DATA"
     style="width: 100%" />

**PREPROCESSING STEPS**
- Categorize activities to more defined activites
- Collect readings (sensor, value, activity) into a list,
- map Categorized activites to the activities list and them numericalize them (encode).
- tokenize and numericalize sensor activations (sensor + value)
- map activities to sequences of sensor activations that caused the activity
- pad sequences to same length

*INFO: The sensor events are generated from motion sensors (these sensor IDs begin with "M") and
temperature sensors (these sensor IDs begin with "T").*  
  
**GROUPING OF SIMILAR ACTIVITIES**   
  
Activity mapping based on common sensor activations:

| Activity      | Group     |
| :---          |          ---: |
| Breakfast | Eat |
| Bed to toilet | Use Toilet |
| R1 sleep | Sleep |
| R1 wake | Wake up |
| R1 work in office | Work |
| Dinner | Eat |
| Laundry | Laundry |
| Leave home | Exit |
| Lunch | Eat |
| Night wandering | Others |
| R2 sleep | Sleep |
| R2 take medicine | Counter |
| R2 wake | Wake up |