# Numerical Optimization Project

## Python GUI application for Numerical optimization

Numerical Optimization Project is a GUI framework for executing and testing different unconstrained optimization algorithms in Python.The application contains a library of various test functions with pre-defined starting points. A several known classes of methods as well as different classes of line search procedures are covered. This application is easily extensible and contains simple API for adding new functions, methods and line searches. 

To run the application just run **main.py** file

![Screenshot 2024-09-27 160325](https://github.com/user-attachments/assets/8b678deb-6494-4405-938a-b568d5ed343c)

### Adding new functions

Functions are located in the Functions folder. To add a new function, it is necessary to create a new Python file in that folder and implement the desired function in it. It is recommended that the name of the file be the name of the added function so that some other users can easily see which functions have already been added in this application, in order to avoid duplication. After adding the file in the Functions folder, it is necessary to import that function in the main_controller file.


### Adding new Line Search methods

Line search methods are located in the LineSearch folder. To add a new line search method, you need to create a new Python file in that folder. It is recommended that the file name be the name of the line search method you want to implement. It is necessary to inherit the abstract class from the line_search file, which is also located in that folder, and modify it. In that file, you need to import the EvaluationNumber class from the Utils folder, with the help of which you will return the number of evaluations. Then you need to import that new method in the line_search_factory file located in the LineSearch folder.


### Adding new methods

The methods are located in the Methods folder. According to the group they belong to, they are divided into 6 folders. Depending on which group they belong to, you will create a new Python file in that folder. It is recommended that the name of that file be the name of that method. To add a new method, you need to import the OptimizationMethod class, which is located in the optimization_methods file in the Utils folder. It represents a template for new methods. You should also import the EvaluationNumber class from the evaluation_number file from the Utils folder and use it to count evaluations. After implementing the new method, it is necessary to go to the main_controller file and import the new method there.




