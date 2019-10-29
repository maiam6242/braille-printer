EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Conn_01x07_Male Arduino-StepperControl1
U 1 1 5DB9AA25
P 2100 5750
F 0 "Arduino-StepperControl1" H 2208 6231 50  0000 C CNN
F 1 "Conn_01x07_Male" H 2208 6140 50  0000 C CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_1x07_P2.00mm_Vertical" H 2100 5750 50  0001 C CNN
F 3 "~" H 2100 5750 50  0001 C CNN
	1    2100 5750
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x02_Male 12Vin1
U 1 1 5DB9E89A
P 1100 5650
F 0 "12Vin1" H 1208 5831 50  0000 C CNN
F 1 "Conn_01x02_Male" H 1208 5740 50  0000 C CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_1x02_P2.00mm_Vertical" H 1100 5650 50  0001 C CNN
F 3 "~" H 1100 5650 50  0001 C CNN
	1    1100 5650
	1    0    0    -1  
$EndComp
$Comp
L CustomSymbols:STSPIN820 U2
U 1 1 5DBB0CCE
P 3150 5950
F 0 "U2" H 3350 6065 50  0000 C CNN
F 1 "STSPIN820" H 3350 5974 50  0000 C CNN
F 2 "" H 3350 5000 50  0001 C CNN
F 3 "" H 3350 5000 50  0001 C CNN
	1    3150 5950
	1    0    0    -1  
$EndComp
$Comp
L CustomSymbols:STSPIN820 U1
U 1 1 5DBB213D
P 3150 4400
F 0 "U1" H 3350 4515 50  0000 C CNN
F 1 "STSPIN820" H 3350 4424 50  0000 C CNN
F 2 "" H 3350 3450 50  0001 C CNN
F 3 "" H 3350 3450 50  0001 C CNN
	1    3150 4400
	1    0    0    -1  
$EndComp
Text GLabel 3800 4650 2    50   Input ~ 0
GND
Text GLabel 11100 4050 2    50   Input ~ 0
12V
Wire Wire Line
	10950 4050 11100 4050
Text GLabel 1300 5650 2    50   Input ~ 0
12V
Text GLabel 1300 5750 2    50   Input ~ 0
GND
Text GLabel 950  6500 2    50   Input ~ 0
12V
Text GLabel 950  6600 2    50   Input ~ 0
GND
Text GLabel 8850 600  0    50   Input ~ 0
GND
Text GLabel 8550 1000 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R14
U 1 1 5DBA96E2
P 8450 800
F 0 "R14" H 8509 846 50  0000 L CNN
F 1 "R_Small" H 8509 755 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 8450 800 50  0001 C CNN
F 3 "~" H 8450 800 50  0001 C CNN
	1    8450 800 
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D14
U 1 1 5DBA8538
P 8700 1000
F 0 "D14" H 8700 1216 50  0000 C CNN
F 1 "1N4003" H 8700 1125 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 8700 825 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 8700 1000 50  0001 C CNN
	1    8700 1000
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q14
U 1 1 5DBA0557
P 8750 800
F 0 "Q14" H 8956 846 50  0000 L CNN
F 1 "DMN6140L" H 8956 755 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223" H 8950 725 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8750 800 50  0001 L CNN
	1    8750 800 
	1    0    0    -1  
$EndComp
Text GLabel 8100 950  0    50   Input ~ 0
GND
Text GLabel 7800 1350 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R7
U 1 1 5DC2ED6F
P 7700 1150
F 0 "R7" H 7759 1196 50  0000 L CNN
F 1 "R_Small" H 7759 1105 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 7700 1150 50  0001 C CNN
F 3 "~" H 7700 1150 50  0001 C CNN
	1    7700 1150
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D7
U 1 1 5DC2ED75
P 7950 1350
F 0 "D7" H 7950 1566 50  0000 C CNN
F 1 "1N4003" H 7950 1475 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 7950 1175 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 7950 1350 50  0001 C CNN
	1    7950 1350
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q7
U 1 1 5DC2ED7B
P 8000 1150
F 0 "Q7" H 8206 1196 50  0000 L CNN
F 1 "DMN6140L" H 8206 1105 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223" H 8200 1075 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8000 1150 50  0001 L CNN
	1    8000 1150
	1    0    0    -1  
$EndComp
Text GLabel 8800 1450 0    50   Input ~ 0
GND
Text GLabel 8500 1850 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R11
U 1 1 5DC3F63E
P 8400 1650
F 0 "R11" H 8459 1696 50  0000 L CNN
F 1 "R_Small" H 8459 1605 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 8400 1650 50  0001 C CNN
F 3 "~" H 8400 1650 50  0001 C CNN
	1    8400 1650
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D11
U 1 1 5DC3F644
P 8650 1850
F 0 "D11" H 8650 2066 50  0000 C CNN
F 1 "1N4003" H 8650 1975 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 8650 1675 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 8650 1850 50  0001 C CNN
	1    8650 1850
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q11
U 1 1 5DC3F64A
P 8700 1650
F 0 "Q11" H 8906 1696 50  0000 L CNN
F 1 "DMN6140L" H 8906 1605 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223" H 8900 1575 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8700 1650 50  0001 L CNN
	1    8700 1650
	1    0    0    -1  
$EndComp
Text GLabel 8050 1800 0    50   Input ~ 0
GND
Text GLabel 7750 2200 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R4
U 1 1 5DC3F652
P 7650 2000
F 0 "R4" H 7709 2046 50  0000 L CNN
F 1 "R_Small" H 7709 1955 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 7650 2000 50  0001 C CNN
F 3 "~" H 7650 2000 50  0001 C CNN
	1    7650 2000
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D4
U 1 1 5DC3F658
P 7900 2200
F 0 "D4" H 7900 2416 50  0000 C CNN
F 1 "1N4003" H 7900 2325 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 7900 2025 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 7900 2200 50  0001 C CNN
	1    7900 2200
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q4
U 1 1 5DC3F65E
P 7950 2000
F 0 "Q4" H 8156 2046 50  0000 L CNN
F 1 "DMN6140L" H 8156 1955 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223" H 8150 1925 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 7950 2000 50  0001 L CNN
	1    7950 2000
	1    0    0    -1  
$EndComp
Text GLabel 8800 2300 0    50   Input ~ 0
GND
Text GLabel 8500 2700 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R12
U 1 1 5DC43ED1
P 8400 2500
F 0 "R12" H 8459 2546 50  0000 L CNN
F 1 "R_Small" H 8459 2455 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 8400 2500 50  0001 C CNN
F 3 "~" H 8400 2500 50  0001 C CNN
	1    8400 2500
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D12
U 1 1 5DC43ED7
P 8650 2700
F 0 "D12" H 8650 2916 50  0000 C CNN
F 1 "1N4003" H 8650 2825 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 8650 2525 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 8650 2700 50  0001 C CNN
	1    8650 2700
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q12
U 1 1 5DC43EDD
P 8700 2500
F 0 "Q12" H 8906 2546 50  0000 L CNN
F 1 "DMN6140L" H 8906 2455 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223" H 8900 2425 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8700 2500 50  0001 L CNN
	1    8700 2500
	1    0    0    -1  
$EndComp
Text GLabel 8050 2650 0    50   Input ~ 0
GND
Text GLabel 7750 3050 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R5
U 1 1 5DC43EE5
P 7650 2850
F 0 "R5" H 7709 2896 50  0000 L CNN
F 1 "R_Small" H 7709 2805 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 7650 2850 50  0001 C CNN
F 3 "~" H 7650 2850 50  0001 C CNN
	1    7650 2850
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D5
U 1 1 5DC43EEB
P 7900 3050
F 0 "D5" H 7900 3266 50  0000 C CNN
F 1 "1N4003" H 7900 3175 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 7900 2875 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 7900 3050 50  0001 C CNN
	1    7900 3050
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q5
U 1 1 5DC43EF1
P 7950 2850
F 0 "Q5" H 8156 2896 50  0000 L CNN
F 1 "DMN6140L" H 8156 2805 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223" H 8150 2775 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 7950 2850 50  0001 L CNN
	1    7950 2850
	1    0    0    -1  
$EndComp
Text GLabel 8800 3150 0    50   Input ~ 0
GND
Text GLabel 8500 3550 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R13
U 1 1 5DC486DC
P 8400 3350
F 0 "R13" H 8459 3396 50  0000 L CNN
F 1 "R_Small" H 8459 3305 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 8400 3350 50  0001 C CNN
F 3 "~" H 8400 3350 50  0001 C CNN
	1    8400 3350
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D13
U 1 1 5DC486E2
P 8650 3550
F 0 "D13" H 8650 3766 50  0000 C CNN
F 1 "1N4003" H 8650 3675 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 8650 3375 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 8650 3550 50  0001 C CNN
	1    8650 3550
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q13
U 1 1 5DC486E8
P 8700 3350
F 0 "Q13" H 8906 3396 50  0000 L CNN
F 1 "DMN6140L" H 8906 3305 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223" H 8900 3275 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8700 3350 50  0001 L CNN
	1    8700 3350
	1    0    0    -1  
$EndComp
Text GLabel 8050 3500 0    50   Input ~ 0
GND
Text GLabel 7750 3900 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R6
U 1 1 5DC486F0
P 7650 3700
F 0 "R6" H 7709 3746 50  0000 L CNN
F 1 "R_Small" H 7709 3655 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 7650 3700 50  0001 C CNN
F 3 "~" H 7650 3700 50  0001 C CNN
	1    7650 3700
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D6
U 1 1 5DC486F6
P 7900 3900
F 0 "D6" H 7900 4116 50  0000 C CNN
F 1 "1N4003" H 7900 4025 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 7900 3725 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 7900 3900 50  0001 C CNN
	1    7900 3900
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q6
U 1 1 5DC486FC
P 7950 3700
F 0 "Q6" H 8156 3746 50  0000 L CNN
F 1 "DMN6140L" H 8156 3655 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223" H 8150 3625 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 7950 3700 50  0001 L CNN
	1    7950 3700
	1    0    0    -1  
$EndComp
Text GLabel 8750 4000 0    50   Input ~ 0
GND
Text GLabel 8450 4400 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R10
U 1 1 5DC67359
P 8350 4200
F 0 "R10" H 8409 4246 50  0000 L CNN
F 1 "R_Small" H 8409 4155 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 8350 4200 50  0001 C CNN
F 3 "~" H 8350 4200 50  0001 C CNN
	1    8350 4200
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D10
U 1 1 5DC6735F
P 8600 4400
F 0 "D10" H 8600 4616 50  0000 C CNN
F 1 "1N4003" H 8600 4525 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 8600 4225 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 8600 4400 50  0001 C CNN
	1    8600 4400
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q10
U 1 1 5DC67365
P 8650 4200
F 0 "Q10" H 8856 4246 50  0000 L CNN
F 1 "DMN6140L" H 8856 4155 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223" H 8850 4125 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8650 4200 50  0001 L CNN
	1    8650 4200
	1    0    0    -1  
$EndComp
Text GLabel 8000 4350 0    50   Input ~ 0
GND
Text GLabel 7700 4750 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R3
U 1 1 5DC6736D
P 7600 4550
F 0 "R3" H 7659 4596 50  0000 L CNN
F 1 "R_Small" H 7659 4505 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 7600 4550 50  0001 C CNN
F 3 "~" H 7600 4550 50  0001 C CNN
	1    7600 4550
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D3
U 1 1 5DC67373
P 7850 4750
F 0 "D3" H 7850 4966 50  0000 C CNN
F 1 "1N4003" H 7850 4875 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 7850 4575 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 7850 4750 50  0001 C CNN
	1    7850 4750
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q3
U 1 1 5DC67379
P 7900 4550
F 0 "Q3" H 8106 4596 50  0000 L CNN
F 1 "DMN6140L" H 8106 4505 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223" H 8100 4475 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 7900 4550 50  0001 L CNN
	1    7900 4550
	1    0    0    -1  
$EndComp
Text GLabel 8700 4850 0    50   Input ~ 0
GND
Text GLabel 8400 5250 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R8
U 1 1 5DC67381
P 8300 5050
F 0 "R8" H 8359 5096 50  0000 L CNN
F 1 "R_Small" H 8359 5005 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 8300 5050 50  0001 C CNN
F 3 "~" H 8300 5050 50  0001 C CNN
	1    8300 5050
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D8
U 1 1 5DC67387
P 8550 5250
F 0 "D8" H 8550 5466 50  0000 C CNN
F 1 "1N4003" H 8550 5375 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 8550 5075 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 8550 5250 50  0001 C CNN
	1    8550 5250
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q8
U 1 1 5DC6738D
P 8600 5050
F 0 "Q8" H 8806 5096 50  0000 L CNN
F 1 "DMN6140L" H 8806 5005 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223" H 8800 4975 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8600 5050 50  0001 L CNN
	1    8600 5050
	1    0    0    -1  
$EndComp
Text GLabel 7950 5200 0    50   Input ~ 0
GND
Text GLabel 7650 5600 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R1
U 1 1 5DC67395
P 7550 5400
F 0 "R1" H 7609 5446 50  0000 L CNN
F 1 "R_Small" H 7609 5355 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 7550 5400 50  0001 C CNN
F 3 "~" H 7550 5400 50  0001 C CNN
	1    7550 5400
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D1
U 1 1 5DC6739B
P 7800 5600
F 0 "D1" H 7800 5816 50  0000 C CNN
F 1 "1N4003" H 7800 5725 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 7800 5425 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 7800 5600 50  0001 C CNN
	1    7800 5600
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q1
U 1 1 5DC673A1
P 7850 5400
F 0 "Q1" H 8056 5446 50  0000 L CNN
F 1 "DMN6140L" H 8056 5355 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223" H 8050 5325 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 7850 5400 50  0001 L CNN
	1    7850 5400
	1    0    0    -1  
$EndComp
Text GLabel 8700 5700 0    50   Input ~ 0
GND
Text GLabel 8400 6100 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R9
U 1 1 5DC673A9
P 8300 5900
F 0 "R9" H 8359 5946 50  0000 L CNN
F 1 "R_Small" H 8359 5855 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 8300 5900 50  0001 C CNN
F 3 "~" H 8300 5900 50  0001 C CNN
	1    8300 5900
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D9
U 1 1 5DC673AF
P 8550 6100
F 0 "D9" H 8550 6316 50  0000 C CNN
F 1 "1N4003" H 8550 6225 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 8550 5925 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 8550 6100 50  0001 C CNN
	1    8550 6100
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q9
U 1 1 5DC673B5
P 8600 5900
F 0 "Q9" H 8806 5946 50  0000 L CNN
F 1 "DMN6140L" H 8806 5855 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223" H 8800 5825 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8600 5900 50  0001 L CNN
	1    8600 5900
	1    0    0    -1  
$EndComp
Text GLabel 7950 6050 0    50   Input ~ 0
GND
Text GLabel 7650 6450 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R2
U 1 1 5DC673BD
P 7550 6250
F 0 "R2" H 7609 6296 50  0000 L CNN
F 1 "R_Small" H 7609 6205 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 7550 6250 50  0001 C CNN
F 3 "~" H 7550 6250 50  0001 C CNN
	1    7550 6250
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D2
U 1 1 5DC673C3
P 7800 6450
F 0 "D2" H 7800 6666 50  0000 C CNN
F 1 "1N4003" H 7800 6575 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 7800 6275 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 7800 6450 50  0001 C CNN
	1    7800 6450
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q2
U 1 1 5DC673C9
P 7850 6250
F 0 "Q2" H 8056 6296 50  0000 L CNN
F 1 "DMN6140L" H 8056 6205 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-223" H 8050 6175 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 7850 6250 50  0001 L CNN
	1    7850 6250
	1    0    0    -1  
$EndComp
Text GLabel 7550 7500 0    50   Input ~ 0
12V
Wire Wire Line
	8850 1000 10450 1000
Wire Wire Line
	10450 1000 10450 2750
Connection ~ 8850 1000
Wire Wire Line
	8100 1350 10400 1350
Wire Wire Line
	10400 1350 10400 2850
Wire Wire Line
	10400 2850 10450 2850
Connection ~ 8100 1350
Wire Wire Line
	8800 1850 10350 1850
Wire Wire Line
	10350 1850 10350 2950
Wire Wire Line
	10350 2950 10450 2950
Connection ~ 8800 1850
Wire Wire Line
	8050 2200 10300 2200
Wire Wire Line
	10300 2200 10300 3050
Wire Wire Line
	10300 3050 10450 3050
Connection ~ 8050 2200
Wire Wire Line
	8800 2700 10250 2700
Wire Wire Line
	10250 2700 10250 3150
Wire Wire Line
	10250 3150 10450 3150
Connection ~ 8800 2700
Wire Wire Line
	8050 3050 10200 3050
Wire Wire Line
	10200 3050 10200 3250
Wire Wire Line
	10200 3250 10450 3250
Connection ~ 8050 3050
Wire Wire Line
	7950 6450 10450 6450
Wire Wire Line
	10450 6450 10450 4050
Connection ~ 7950 6450
Wire Wire Line
	8700 6100 10400 6100
Wire Wire Line
	10400 6100 10400 3950
Wire Wire Line
	10400 3950 10450 3950
Connection ~ 8700 6100
Wire Wire Line
	7950 5600 10350 5600
Wire Wire Line
	10350 5600 10350 3850
Wire Wire Line
	10350 3850 10450 3850
Connection ~ 7950 5600
Wire Wire Line
	8700 5250 10300 5250
Wire Wire Line
	10300 5250 10300 3750
Wire Wire Line
	10300 3750 10450 3750
Connection ~ 8700 5250
Wire Wire Line
	8000 4750 10250 4750
Wire Wire Line
	10250 4750 10250 3650
Wire Wire Line
	10250 3650 10450 3650
Connection ~ 8000 4750
Wire Wire Line
	8750 4400 10200 4400
Wire Wire Line
	10200 4400 10200 3550
Wire Wire Line
	10200 3550 10450 3550
Connection ~ 8750 4400
Wire Wire Line
	8050 3900 10150 3900
Wire Wire Line
	10150 3900 10150 3450
Wire Wire Line
	10150 3450 10450 3450
Connection ~ 8050 3900
Wire Wire Line
	8800 3550 10100 3550
Wire Wire Line
	10100 3550 10100 3350
Wire Wire Line
	10100 3350 10450 3350
Connection ~ 8800 3550
Wire Wire Line
	8350 800  6150 800 
Wire Wire Line
	7600 1150 6250 1150
Wire Wire Line
	8300 1650 6350 1650
Wire Wire Line
	7550 2000 6450 2000
Wire Wire Line
	8300 2500 6550 2500
Wire Wire Line
	7550 2850 6650 2850
Wire Wire Line
	6150 800  6150 3250
Wire Wire Line
	6250 1150 6250 3250
Wire Wire Line
	6350 1650 6350 3250
Wire Wire Line
	6450 2000 6450 3250
Wire Wire Line
	6550 2500 6550 3250
Wire Wire Line
	6650 2850 6650 3250
Wire Wire Line
	8300 3350 6850 3350
Wire Wire Line
	6850 3350 6850 3250
Wire Wire Line
	6850 3250 6750 3250
Wire Wire Line
	7550 3700 6850 3700
Wire Wire Line
	6850 3700 6850 3750
Wire Wire Line
	6850 3750 6750 3750
Wire Wire Line
	8250 4200 6650 4200
Wire Wire Line
	6650 4200 6650 3750
Wire Wire Line
	7500 4550 6550 4550
Wire Wire Line
	6550 4550 6550 3750
Wire Wire Line
	8200 5050 6450 5050
Wire Wire Line
	6450 5050 6450 3750
Wire Wire Line
	7450 5400 6350 5400
Wire Wire Line
	6350 5400 6350 3750
Wire Wire Line
	8200 5900 6250 5900
Wire Wire Line
	6250 5900 6250 3750
Wire Wire Line
	7450 6250 6150 6250
Wire Wire Line
	6150 6250 6150 3750
Text GLabel 3800 6800 2    50   Input ~ 0
GND
Text GLabel 3800 6200 2    50   Input ~ 0
GND
Text GLabel 3800 5250 2    50   Input ~ 0
GND
Text GLabel 3800 5150 2    50   Input ~ 0
5V
Text GLabel 3800 6700 2    50   Input ~ 0
5V
$Comp
L Connector:Conn_01x03_Male ArduinoPower1
U 1 1 5DD3A23F
P 750 6600
F 0 "ArduinoPower1" H 858 6881 50  0000 C CNN
F 1 "Conn_01x03_Male" H 858 6790 50  0000 C CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_1x03_P2.00mm_Vertical" H 750 6600 50  0001 C CNN
F 3 "~" H 750 6600 50  0001 C CNN
	1    750  6600
	1    0    0    -1  
$EndComp
Text GLabel 950  6700 2    50   Input ~ 0
5V
Text GLabel 3800 4550 2    50   Input ~ 0
12V
Text GLabel 3800 6100 2    50   Input ~ 0
12V
Wire Wire Line
	3800 4750 4600 4750
Wire Wire Line
	4600 4750 4600 5450
Wire Wire Line
	3800 4850 4500 4850
Wire Wire Line
	4500 4850 4500 5450
Wire Wire Line
	3800 4950 4400 4950
Wire Wire Line
	4400 4950 4400 5450
Wire Wire Line
	3800 5050 4300 5050
Wire Wire Line
	4300 5050 4300 5450
Wire Wire Line
	3800 6600 4300 6600
Wire Wire Line
	4300 6600 4300 5950
Wire Wire Line
	3800 6500 4400 6500
Wire Wire Line
	4400 6500 4400 5950
Wire Wire Line
	3800 6400 4500 6400
Wire Wire Line
	4500 6400 4500 5950
Wire Wire Line
	3800 6300 4600 6300
Wire Wire Line
	4600 6300 4600 5950
Wire Wire Line
	2300 5650 2900 5650
Wire Wire Line
	2900 5650 2900 5250
Wire Wire Line
	2300 5550 2850 5550
Wire Wire Line
	2850 5550 2850 5150
Wire Wire Line
	2850 5150 2900 5150
Wire Wire Line
	2300 5450 2450 5450
Wire Wire Line
	2450 5450 2450 4550
Wire Wire Line
	2450 4550 2900 4550
NoConn ~ 2900 4950
NoConn ~ 2900 5050
NoConn ~ 2900 6500
NoConn ~ 2900 6600
Wire Wire Line
	2300 5750 2900 5750
Wire Wire Line
	2900 5750 2900 6100
Wire Wire Line
	2300 5850 2450 5850
Wire Wire Line
	2450 5850 2450 6700
Wire Wire Line
	2450 6700 2900 6700
Wire Wire Line
	2300 5950 2400 5950
Wire Wire Line
	2400 5950 2400 6800
Wire Wire Line
	2400 6800 2900 6800
$Comp
L Connector:Conn_01x02_Male HomeSwitch1
U 1 1 5DDC4700
P 1550 7000
F 0 "HomeSwitch1" H 1658 7181 50  0000 C CNN
F 1 "Conn_01x02_Male" H 1658 7090 50  0000 C CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_1x02_P2.00mm_Vertical" H 1550 7000 50  0001 C CNN
F 3 "~" H 1550 7000 50  0001 C CNN
	1    1550 7000
	1    0    0    -1  
$EndComp
Wire Wire Line
	1750 7000 2300 7000
Wire Wire Line
	2300 7000 2300 6050
Text GLabel 1750 7100 2    50   Input ~ 0
GND
Text GLabel 2900 4650 0    50   Input ~ 0
GND
Text GLabel 2900 4750 0    50   Input ~ 0
GND
Text GLabel 2900 4850 0    50   Input ~ 0
GND
Text GLabel 2900 6200 0    50   Input ~ 0
GND
Text GLabel 2900 6300 0    50   Input ~ 0
GND
Text GLabel 2900 6400 0    50   Input ~ 0
GND
$Comp
L Connector_Generic:Conn_02x07_Odd_Even Arduino-SolenoidControl1
U 1 1 5DDF6ADB
P 6450 3550
F 0 "Arduino-SolenoidControl1" H 6500 4067 50  0000 C CNN
F 1 "Conn_02x07_Odd_Even" H 6500 3976 50  0000 C CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_2x07_P2.00mm_Vertical" H 6450 3550 50  0001 C CNN
F 3 "~" H 6450 3550 50  0001 C CNN
	1    6450 3550
	0    -1   -1   0   
$EndComp
$Comp
L Connector_Generic:Conn_02x14_Odd_Even SolenoidOut1
U 1 1 5DE02A66
P 10650 3350
F 0 "SolenoidOut1" H 10700 4167 50  0000 C CNN
F 1 "Conn_02x14_Odd_Even" H 10700 4076 50  0000 C CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_2x14_P2.00mm_Vertical" H 10650 3350 50  0001 C CNN
F 3 "~" H 10650 3350 50  0001 C CNN
	1    10650 3350
	1    0    0    -1  
$EndComp
Wire Wire Line
	10950 3950 10950 4050
Connection ~ 10950 4050
Wire Wire Line
	10950 2750 10950 2850
Connection ~ 10950 2850
Wire Wire Line
	10950 2850 10950 2950
Connection ~ 10950 2950
Wire Wire Line
	10950 2950 10950 3050
Connection ~ 10950 3050
Wire Wire Line
	10950 3050 10950 3150
Connection ~ 10950 3150
Wire Wire Line
	10950 3150 10950 3250
Connection ~ 10950 3250
Wire Wire Line
	10950 3250 10950 3350
Connection ~ 10950 3350
Wire Wire Line
	10950 3350 10950 3450
Connection ~ 10950 3450
Wire Wire Line
	10950 3450 10950 3550
Connection ~ 10950 3550
Wire Wire Line
	10950 3550 10950 3650
Connection ~ 10950 3650
Wire Wire Line
	10950 3650 10950 3750
Connection ~ 10950 3750
Wire Wire Line
	10950 3750 10950 3850
Connection ~ 10950 3850
Wire Wire Line
	10950 3850 10950 3950
Connection ~ 10950 3950
$Comp
L Connector_Generic:Conn_02x04_Odd_Even StepperOut1
U 1 1 5DE15327
P 4400 5750
F 0 "StepperOut1" H 4450 6067 50  0000 C CNN
F 1 "Conn_02x04_Odd_Even" H 4450 5976 50  0000 C CNN
F 2 "Connector_PinHeader_2.00mm:PinHeader_2x04_P2.00mm_Vertical" H 4400 5750 50  0001 C CNN
F 3 "~" H 4400 5750 50  0001 C CNN
	1    4400 5750
	0    -1   -1   0   
$EndComp
$Comp
L Device:C C2
U 1 1 5DE61B2B
P 3800 5950
F 0 "C2" H 3915 5996 50  0000 L CNN
F 1 "C" H 3915 5905 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric" H 3838 5800 50  0001 C CNN
F 3 "~" H 3800 5950 50  0001 C CNN
	1    3800 5950
	1    0    0    -1  
$EndComp
$Comp
L Device:C C1
U 1 1 5DE64DAB
P 3800 4400
F 0 "C1" H 3915 4446 50  0000 L CNN
F 1 "C" H 3915 4355 50  0000 L CNN
F 2 "Capacitor_SMD:C_1206_3216Metric" H 3838 4250 50  0001 C CNN
F 3 "~" H 3800 4400 50  0001 C CNN
	1    3800 4400
	1    0    0    -1  
$EndComp
Text GLabel 3800 4250 2    50   Input ~ 0
GND
Text GLabel 3800 5800 2    50   Input ~ 0
GND
$EndSCHEMATC
