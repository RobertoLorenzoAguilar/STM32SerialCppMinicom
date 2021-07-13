
#Creating a C++ project in nucleo board to keep communication serial USART with a STM Nucleo-F446RE Board 


![f6d5d37f-fd69-4b06-8286-82d5155191a6](https://user-images.githubusercontent.com/48602725/125301926-52860a80-e2e0-11eb-9598-a278fa7f84e7.jpg)



remember dowload the usb driver in the oficial stm32 page in my model case is the https://www.st.com/content/st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-utilities/stsw-link009.html


also, you will need have installed the STM32CubeIDE through which you will program your app https://www.st.com/en/development-tools/stm32cubeide.html


once time that you have finished satisfactory the STM32Cube IDE, you should select the target

![image](https://user-images.githubusercontent.com/48602725/125303149-7269fe00-e2e1-11eb-95ee-162089563139.png)



set a name to the project and select in the checkbox the type to of final language in this example case I chose CPP.

![image](https://user-images.githubusercontent.com/48602725/125303383-9d545200-e2e1-11eb-880c-303b15e587f1.png)

as soon you created the project will appear a window with an .ioc file open in which you should enable the pins to carry up the serial communication.

![image](https://user-images.githubusercontent.com/48602725/125304465-78acaa00-e2e2-11eb-9900-ab772a6a1bdb.png)


remember rename in Core/Src/main.c to main.cpp such a:

![image](https://user-images.githubusercontent.com/48602725/125304819-bdd0dc00-e2e2-11eb-88f8-bcc229d69201.png)


and then you can start to program, I could create  one program to calculate the square of number.

![image](https://user-images.githubusercontent.com/48602725/125461232-e3d63e61-ca31-4fdd-beb5-21dbe41104d7.png)




![image](https://user-images.githubusercontent.com/48602725/125197963-b511d480-e214-11eb-8766-f8fe53f0db30.png)

references----> http://www.coffeebrain.org/wiki/index.php?title=USART_B%C3%A1sico


test the serial communication. although exist  PUTTY and TERATERM to establish and test connection serial with our board I prefer minicom,I reccomend that you have install a window subsystem linux, here you can find the steps to will install the app https://docs.microsoft.com/es-es/windows/wsl/install-win10  and after install the minicom 

I installed the Ubuntu 20.04 LTS release on Windows, in this new version you don't need use the apt-get only the apt in the (Focal Fossa) version, obviously you can choose the Linux version os with you to feel comfortable "remember update and upgrade"

Note: you can find the source path of wsl in \\wsl$ 
![image](https://user-images.githubusercontent.com/48602725/125330881-26788280-e2fc-11eb-91e7-a836ea43905b.png)



~~~
 sudo apt update && sudo apt upgrade -y
 sudo apt  install minicom 
~~~

to run a minicom interface you need to type the following command 
~~~
sudo minicom -s.

~~~
![image](https://user-images.githubusercontent.com/48602725/125220799-1b7e0d80-e27c-11eb-8f22-99a4a30057ca.png)


remember that you shall set the virtual COM port, and you can find in the device manager.
![image](https://user-images.githubusercontent.com/48602725/125220616-e2459d80-e27b-11eb-84f3-e95c544bb5ad.png)


![image](https://user-images.githubusercontent.com/48602725/125220979-5ed87c00-e27c-11eb-82c2-7651508c0682.png)


![image](https://user-images.githubusercontent.com/48602725/125221031-7283e280-e27c-11eb-9232-26085c22d39f.png)


you also need to set the main params, 115,200 baud rate, and the port COM5 in my case, note: if you will have problems interacting with the board, if you can't see whatever that you write change opcion F and G selecting Flow Control to no.

~~~
serial device :  /dev/ttyS5

~~~

![image](https://user-images.githubusercontent.com/48602725/125221270-d9090080-e27c-11eb-8410-b63eaf6d81ea.png)

Save the changes.
![image](https://user-images.githubusercontent.com/48602725/125221977-f8545d80-e27d-11eb-8d01-d7f02c7818aa.png)


And then if all was good you will see the minicom interface

![image](https://user-images.githubusercontent.com/48602725/125222077-2f2a7380-e27e-11eb-8b87-06bd105fe147.png)

If you can try again to the minicom interface you only need put: 
~~~
sudo minicom

~~~

As of now you can interact with the board.



TODO: Pending by load.
~~~
1.- the references.
2.- STM32 code.cpp UART communication. By the moment, I couldn't compile the project, I need to learn about of Cortex-M4  :S, I wanted to incorporate the activities with process STM Board , to recreating A scenery a little more real,  I leave in stand by
g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC  main.cpp -I../Inc -I../../Drivers/STM32F4xx_HAL_Driver/Inc -I../../Drivers/CMSIS/Device/ST/STM32F4xx/Include -D STM32F446xx  -I../../Drivers/CMSIS/Include  -D __GNUC__   I believe that I need to create a dll to work with the drivers, however, I hope that I hope someone benefits with the information about of how to establish communication serial with this kind of board, probably in the future I change this thread to other repository
~~~
