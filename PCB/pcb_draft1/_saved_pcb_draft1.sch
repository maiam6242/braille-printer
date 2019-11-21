EESchema Schematic File Version 4
LIBS:pcb_draft1-cache
EELAYER 26 0
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
L CustomSymbols:STSPIN820 U2
U 1 1 5DBB0CCE
P 3150 5950
F 0 "U2" H 3350 6065 50  0000 C CNN
F 1 "STSPIN820" H 3350 5974 50  0000 C CNN
F 2 "custom_symbols:stepper_driver" H 3350 5000 50  0001 C CNN
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
F 2 "custom_symbols:stepper_driver" H 3350 3450 50  0001 C CNN
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
Text GLabel 8850 600  0    50   Input ~ 0
GND
Text GLabel 8550 1000 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R15
U 1 1 5DBA96E2
P 6250 800
F 0 "R15" H 6309 846 50  0000 L CNN
F 1 "200_Ohm_R" H 6309 755 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6250 800 50  0001 C CNN
F 3 "~" H 6250 800 50  0001 C CNN
	1    6250 800 
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D1
U 1 1 5DBA8538
P 8700 1000
F 0 "D1" H 8700 1216 50  0000 C CNN
F 1 "1N4003" H 8700 1125 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 8700 825 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 8700 1000 50  0001 C CNN
	1    8700 1000
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q1
U 1 1 5DBA0557
P 8750 800
F 0 "Q1" H 8956 846 50  0000 L CNN
F 1 "DMN6140L" H 8956 755 50  0000 L CNN
F 2 "custom_symbols:SOT-223-edited" H 8950 725 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8750 800 50  0001 L CNN
	1    8750 800 
	1    0    0    -1  
$EndComp
Text GLabel 8100 950  0    50   Input ~ 0
GND
Text GLabel 7800 1350 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R16
U 1 1 5DC2ED6F
P 6350 1150
F 0 "R16" H 6409 1196 50  0000 L CNN
F 1 "200_Ohm_R" H 6409 1105 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6350 1150 50  0001 C CNN
F 3 "~" H 6350 1150 50  0001 C CNN
	1    6350 1150
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D2
U 1 1 5DC2ED75
P 7950 1350
F 0 "D2" H 7950 1566 50  0000 C CNN
F 1 "1N4003" H 7950 1475 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 7950 1175 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 7950 1350 50  0001 C CNN
	1    7950 1350
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q2
U 1 1 5DC2ED7B
P 8000 1150
F 0 "Q2" H 8206 1196 50  0000 L CNN
F 1 "DMN6140L" H 8206 1105 50  0000 L CNN
F 2 "custom_symbols:SOT-223-edited" H 8200 1075 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8000 1150 50  0001 L CNN
	1    8000 1150
	1    0    0    -1  
$EndComp
Text GLabel 8800 1450 0    50   Input ~ 0
GND
Text GLabel 8500 1850 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R17
U 1 1 5DC3F63E
P 6450 1650
F 0 "R17" H 6509 1696 50  0000 L CNN
F 1 "200_Ohm_R" H 6509 1605 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6450 1650 50  0001 C CNN
F 3 "~" H 6450 1650 50  0001 C CNN
	1    6450 1650
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D3
U 1 1 5DC3F644
P 8650 1850
F 0 "D3" H 8650 2066 50  0000 C CNN
F 1 "1N4003" H 8650 1975 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 8650 1675 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 8650 1850 50  0001 C CNN
	1    8650 1850
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q3
U 1 1 5DC3F64A
P 8700 1650
F 0 "Q3" H 8906 1696 50  0000 L CNN
F 1 "DMN6140L" H 8906 1605 50  0000 L CNN
F 2 "custom_symbols:SOT-223-edited" H 8900 1575 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8700 1650 50  0001 L CNN
	1    8700 1650
	1    0    0    -1  
$EndComp
Text GLabel 8050 1800 0    50   Input ~ 0
GND
Text GLabel 7750 2200 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R18
U 1 1 5DC3F652
P 6550 2000
F 0 "R18" H 6609 2046 50  0000 L CNN
F 1 "200_Ohm_R" H 6609 1955 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6550 2000 50  0001 C CNN
F 3 "~" H 6550 2000 50  0001 C CNN
	1    6550 2000
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
F 2 "custom_symbols:SOT-223-edited" H 8150 1925 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 7950 2000 50  0001 L CNN
	1    7950 2000
	1    0    0    -1  
$EndComp
Text GLabel 8800 2300 0    50   Input ~ 0
GND
Text GLabel 8500 2700 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R19
U 1 1 5DC43ED1
P 6650 2500
F 0 "R19" H 6709 2546 50  0000 L CNN
F 1 "200_Ohm_R" H 6709 2455 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6650 2500 50  0001 C CNN
F 3 "~" H 6650 2500 50  0001 C CNN
	1    6650 2500
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D5
U 1 1 5DC43ED7
P 8650 2700
F 0 "D5" H 8650 2916 50  0000 C CNN
F 1 "1N4003" H 8650 2825 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 8650 2525 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 8650 2700 50  0001 C CNN
	1    8650 2700
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q5
U 1 1 5DC43EDD
P 8700 2500
F 0 "Q5" H 8906 2546 50  0000 L CNN
F 1 "DMN6140L" H 8906 2455 50  0000 L CNN
F 2 "custom_symbols:SOT-223-edited" H 8900 2425 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8700 2500 50  0001 L CNN
	1    8700 2500
	1    0    0    -1  
$EndComp
Text GLabel 8050 2650 0    50   Input ~ 0
GND
Text GLabel 7750 3050 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R20
U 1 1 5DC43EE5
P 6750 2850
F 0 "R20" H 6809 2896 50  0000 L CNN
F 1 "200_Ohm_R" H 6809 2805 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6750 2850 50  0001 C CNN
F 3 "~" H 6750 2850 50  0001 C CNN
	1    6750 2850
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D6
U 1 1 5DC43EEB
P 7900 3050
F 0 "D6" H 7900 3266 50  0000 C CNN
F 1 "1N4003" H 7900 3175 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 7900 2875 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 7900 3050 50  0001 C CNN
	1    7900 3050
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q6
U 1 1 5DC43EF1
P 7950 2850
F 0 "Q6" H 8156 2896 50  0000 L CNN
F 1 "DMN6140L" H 8156 2805 50  0000 L CNN
F 2 "custom_symbols:SOT-223-edited" H 8150 2775 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 7950 2850 50  0001 L CNN
	1    7950 2850
	1    0    0    -1  
$EndComp
Text GLabel 8500 3550 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R21
U 1 1 5DC486DC
P 6850 3350
F 0 "R21" H 6909 3396 50  0000 L CNN
F 1 "200_Ohm_R" H 6909 3305 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6850 3350 50  0001 C CNN
F 3 "~" H 6850 3350 50  0001 C CNN
	1    6850 3350
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D7
U 1 1 5DC486E2
P 8650 3550
F 0 "D7" H 8650 3766 50  0000 C CNN
F 1 "1N4003" H 8650 3675 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 8650 3375 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 8650 3550 50  0001 C CNN
	1    8650 3550
	1    0    0    -1  
$EndComp
Text GLabel 8050 3500 0    50   Input ~ 0
GND
Text GLabel 7750 3900 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R22
U 1 1 5DC486F0
P 6950 3700
F 0 "R22" H 7009 3746 50  0000 L CNN
F 1 "200_Ohm_R" H 7009 3655 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6950 3700 50  0001 C CNN
F 3 "~" H 6950 3700 50  0001 C CNN
	1    6950 3700
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D8
U 1 1 5DC486F6
P 7900 3900
F 0 "D8" H 7900 4116 50  0000 C CNN
F 1 "1N4003" H 7900 4025 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 7900 3725 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 7900 3900 50  0001 C CNN
	1    7900 3900
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q8
U 1 1 5DC486FC
P 7950 3700
F 0 "Q8" H 8156 3746 50  0000 L CNN
F 1 "DMN6140L" H 8156 3655 50  0000 L CNN
F 2 "custom_symbols:SOT-223-edited" H 8150 3625 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 7950 3700 50  0001 L CNN
	1    7950 3700
	1    0    0    -1  
$EndComp
Text GLabel 8750 4000 0    50   Input ~ 0
GND
Text GLabel 8450 4400 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R23
U 1 1 5DC67359
P 6750 4200
F 0 "R23" H 6809 4246 50  0000 L CNN
F 1 "200_Ohm_R" H 6809 4155 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6750 4200 50  0001 C CNN
F 3 "~" H 6750 4200 50  0001 C CNN
	1    6750 4200
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D9
U 1 1 5DC6735F
P 8600 4400
F 0 "D9" H 8600 4616 50  0000 C CNN
F 1 "1N4003" H 8600 4525 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 8600 4225 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 8600 4400 50  0001 C CNN
	1    8600 4400
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q9
U 1 1 5DC67365
P 8650 4200
F 0 "Q9" H 8856 4246 50  0000 L CNN
F 1 "DMN6140L" H 8856 4155 50  0000 L CNN
F 2 "custom_symbols:SOT-223-edited" H 8850 4125 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8650 4200 50  0001 L CNN
	1    8650 4200
	1    0    0    -1  
$EndComp
Text GLabel 8000 4350 0    50   Input ~ 0
GND
Text GLabel 7700 4750 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R24
U 1 1 5DC6736D
P 6650 4550
F 0 "R24" H 6709 4596 50  0000 L CNN
F 1 "200_Ohm_R" H 6709 4505 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6650 4550 50  0001 C CNN
F 3 "~" H 6650 4550 50  0001 C CNN
	1    6650 4550
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D10
U 1 1 5DC67373
P 7850 4750
F 0 "D10" H 7850 4966 50  0000 C CNN
F 1 "1N4003" H 7850 4875 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 7850 4575 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 7850 4750 50  0001 C CNN
	1    7850 4750
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q10
U 1 1 5DC67379
P 7900 4550
F 0 "Q10" H 8106 4596 50  0000 L CNN
F 1 "DMN6140L" H 8106 4505 50  0000 L CNN
F 2 "custom_symbols:SOT-223-edited" H 8100 4475 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 7900 4550 50  0001 L CNN
	1    7900 4550
	1    0    0    -1  
$EndComp
Text GLabel 8700 4850 0    50   Input ~ 0
GND
Text GLabel 8400 5250 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R25
U 1 1 5DC67381
P 6550 5050
F 0 "R25" H 6609 5096 50  0000 L CNN
F 1 "200_Ohm_R" H 6609 5005 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6550 5050 50  0001 C CNN
F 3 "~" H 6550 5050 50  0001 C CNN
	1    6550 5050
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D11
U 1 1 5DC67387
P 8550 5250
F 0 "D11" H 8550 5466 50  0000 C CNN
F 1 "1N4003" H 8550 5375 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 8550 5075 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 8550 5250 50  0001 C CNN
	1    8550 5250
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q11
U 1 1 5DC6738D
P 8600 5050
F 0 "Q11" H 8806 5096 50  0000 L CNN
F 1 "DMN6140L" H 8806 5005 50  0000 L CNN
F 2 "custom_symbols:SOT-223-edited" H 8800 4975 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8600 5050 50  0001 L CNN
	1    8600 5050
	1    0    0    -1  
$EndComp
Text GLabel 7950 5200 0    50   Input ~ 0
GND
Text GLabel 7650 5600 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R26
U 1 1 5DC67395
P 6450 5400
F 0 "R26" H 6509 5446 50  0000 L CNN
F 1 "200_Ohm_R" H 6509 5355 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6450 5400 50  0001 C CNN
F 3 "~" H 6450 5400 50  0001 C CNN
	1    6450 5400
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D12
U 1 1 5DC6739B
P 7800 5600
F 0 "D12" H 7800 5816 50  0000 C CNN
F 1 "1N4003" H 7800 5725 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 7800 5425 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 7800 5600 50  0001 C CNN
	1    7800 5600
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q12
U 1 1 5DC673A1
P 7850 5400
F 0 "Q12" H 8056 5446 50  0000 L CNN
F 1 "DMN6140L" H 8056 5355 50  0000 L CNN
F 2 "custom_symbols:SOT-223-edited" H 8050 5325 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 7850 5400 50  0001 L CNN
	1    7850 5400
	1    0    0    -1  
$EndComp
Text GLabel 8700 5700 0    50   Input ~ 0
GND
Text GLabel 8400 6100 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R27
U 1 1 5DC673A9
P 6350 5900
F 0 "R27" H 6409 5946 50  0000 L CNN
F 1 "200_Ohm_R" H 6409 5855 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6350 5900 50  0001 C CNN
F 3 "~" H 6350 5900 50  0001 C CNN
	1    6350 5900
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D13
U 1 1 5DC673AF
P 8550 6100
F 0 "D13" H 8550 6316 50  0000 C CNN
F 1 "1N4003" H 8550 6225 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 8550 5925 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 8550 6100 50  0001 C CNN
	1    8550 6100
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q13
U 1 1 5DC673B5
P 8600 5900
F 0 "Q13" H 8806 5946 50  0000 L CNN
F 1 "DMN6140L" H 8806 5855 50  0000 L CNN
F 2 "custom_symbols:SOT-223-edited" H 8800 5825 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8600 5900 50  0001 L CNN
	1    8600 5900
	1    0    0    -1  
$EndComp
Text GLabel 7950 6050 0    50   Input ~ 0
GND
Text GLabel 7650 6450 0    50   Input ~ 0
12V
$Comp
L Device:R_Small R28
U 1 1 5DC673BD
P 6250 6250
F 0 "R28" H 6309 6296 50  0000 L CNN
F 1 "200_Ohm_R" H 6309 6205 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6250 6250 50  0001 C CNN
F 3 "~" H 6250 6250 50  0001 C CNN
	1    6250 6250
	0    -1   -1   0   
$EndComp
$Comp
L Diode:1N4003 D14
U 1 1 5DC673C3
P 7800 6450
F 0 "D14" H 7800 6666 50  0000 C CNN
F 1 "1N4003" H 7800 6575 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 7800 6275 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 7800 6450 50  0001 C CNN
	1    7800 6450
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q14
U 1 1 5DC673C9
P 7850 6250
F 0 "Q14" H 8056 6296 50  0000 L CNN
F 1 "DMN6140L" H 8056 6205 50  0000 L CNN
F 2 "custom_symbols:SOT-223-edited" H 8050 6175 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 7850 6250 50  0001 L CNN
	1    7850 6250
	1    0    0    -1  
$EndComp
Wire Wire Line
	10450 1000 10450 2750
Wire Wire Line
	10400 1350 10400 2850
Wire Wire Line
	10400 2850 10450 2850
Wire Wire Line
	10350 1850 10350 2950
Wire Wire Line
	10350 2950 10450 2950
Wire Wire Line
	8050 2200 10300 2200
Wire Wire Line
	10300 2200 10300 3050
Wire Wire Line
	10300 3050 10450 3050
Wire Wire Line
	8800 2700 10250 2700
Wire Wire Line
	10250 2700 10250 3150
Wire Wire Line
	10250 3150 10450 3150
Wire Wire Line
	8050 3050 10200 3050
Wire Wire Line
	10200 3050 10200 3250
Wire Wire Line
	10200 3250 10450 3250
Wire Wire Line
	7950 6450 10450 6450
Wire Wire Line
	10450 6450 10450 4050
Wire Wire Line
	8700 6100 10400 6100
Wire Wire Line
	10400 6100 10400 3950
Wire Wire Line
	10400 3950 10450 3950
Wire Wire Line
	7950 5600 10350 5600
Wire Wire Line
	10350 5600 10350 3850
Wire Wire Line
	10350 3850 10450 3850
Wire Wire Line
	8700 5250 10300 5250
Wire Wire Line
	10300 5250 10300 3750
Wire Wire Line
	10300 3750 10450 3750
Wire Wire Line
	8000 4750 10250 4750
Wire Wire Line
	10250 4750 10250 3650
Wire Wire Line
	10250 3650 10450 3650
Wire Wire Line
	8750 4400 10200 4400
Wire Wire Line
	10200 4400 10200 3550
Wire Wire Line
	10200 3550 10450 3550
Wire Wire Line
	8050 3900 10150 3900
Wire Wire Line
	10150 3900 10150 3450
Wire Wire Line
	10150 3450 10450 3450
Wire Wire Line
	8800 3550 10100 3550
Wire Wire Line
	10100 3550 10100 3350
Wire Wire Line
	10100 3350 10450 3350
Wire Wire Line
	6550 2500 6550 3250
Wire Wire Line
	6550 4550 6550 3750
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
Text GLabel 3800 4550 2    50   Input ~ 0
12V
Text GLabel 3800 6100 2    50   Input ~ 0
12V
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
Text GLabel 1750 7100 2    50   Input ~ 0
GND
Text GLabel 2900 4650 0    50   Input ~ 0
5V
Text GLabel 2900 4750 0    50   Input ~ 0
5V
Text GLabel 2900 4850 0    50   Input ~ 0
GND
Text GLabel 2900 6200 0    50   Input ~ 0
5V
Text GLabel 2900 6300 0    50   Input ~ 0
5V
Text GLabel 2900 6400 0    50   Input ~ 0
GND
$Comp
L Connector_Generic:Conn_02x14_Odd_Even Z1
U 1 1 5DE02A66
P 10650 3350
F 0 "Z1" H 10700 4167 50  0000 C CNN
F 1 "SolenoidOut" H 10700 4076 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x14_P2.54mm_Vertical" H 10650 3350 50  0001 C CNN
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
L Device:C C2
U 1 1 5DE61B2B
P 3800 5950
F 0 "C2" H 3915 5996 50  0000 L CNN
F 1 "C" H 3915 5905 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm" H 3838 5800 50  0001 C CNN
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
F 2 "Capacitor_THT:CP_Radial_D8.0mm_P3.50mm" H 3838 4250 50  0001 C CNN
F 3 "~" H 3800 4400 50  0001 C CNN
	1    3800 4400
	1    0    0    -1  
$EndComp
Text GLabel 3800 4250 2    50   Input ~ 0
GND
Text GLabel 3800 5800 2    50   Input ~ 0
GND
Text GLabel 1900 1650 0    50   Input ~ 0
12V
$Comp
L Diode:1N4003 D15
U 1 1 5DC47CF1
P 2050 1650
F 0 "D15" H 2050 1866 50  0000 C CNN
F 1 "1N4003" H 2050 1775 50  0000 C CNN
F 2 "Diode_THT:D_DO-41_SOD81_P10.16mm_Horizontal" H 2050 1475 50  0001 C CNN
F 3 "http://www.vishay.com/docs/88503/1n4001.pdf" H 2050 1650 50  0001 C CNN
	1    2050 1650
	1    0    0    -1  
$EndComp
$Comp
L Transistor_FET:DMN6140L Q7
U 1 1 5DC486E8
P 8700 3350
F 0 "Q7" H 8906 3396 50  0000 L CNN
F 1 "DMN6140L" H 8906 3305 50  0000 L CNN
F 2 "custom_symbols:SOT-223-edited" H 8900 3275 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 8700 3350 50  0001 L CNN
	1    8700 3350
	1    0    0    -1  
$EndComp
Text GLabel 8800 3150 0    50   Input ~ 0
GND
Text GLabel 2200 1250 0    50   Input ~ 0
GND
$Comp
L Device:R_Small R30
U 1 1 5DC831F8
P 1500 1450
F 0 "R30" H 1559 1496 50  0000 L CNN
F 1 "200_Ohm_R" H 1559 1405 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 1500 1450 50  0001 C CNN
F 3 "~" H 1500 1450 50  0001 C CNN
	1    1500 1450
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2200 1650 2750 1650
$Comp
L Connector:Screw_Terminal_01x02 F1
U 1 1 5DCDDB16
P 2950 1650
F 0 "F1" H 3030 1642 50  0000 L CNN
F 1 "Fan_Screw_Terminal A97996-ND " H 3030 1551 50  0000 L CNN
F 2 "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.00mm_Horizontal" H 2950 1650 50  0001 C CNN
F 3 "~" H 2950 1650 50  0001 C CNN
	1    2950 1650
	1    0    0    -1  
$EndComp
Text GLabel 2750 1750 0    50   Input ~ 0
12V
Wire Wire Line
	2100 2100 2100 2200
Text GLabel 2100 2100 2    50   Input ~ 0
5V
$Comp
L Device:R_Small R31
U 1 1 5DD0CCEA
P 2100 2300
F 0 "R31" H 2159 2346 50  0000 L CNN
F 1 "ThermistorR" H 2159 2255 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 2100 2300 50  0001 C CNN
F 3 "~" H 2100 2300 50  0001 C CNN
	1    2100 2300
	1    0    0    -1  
$EndComp
Wire Wire Line
	2650 2100 2650 2200
Wire Wire Line
	2650 2400 2650 2500
Text GLabel 2650 2100 2    50   Input ~ 0
5V
$Comp
L Device:R_Small R32
U 1 1 5DD55F33
P 2650 2300
F 0 "R32" H 2709 2346 50  0000 L CNN
F 1 "ThermistorR" H 2709 2255 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 2650 2300 50  0001 C CNN
F 3 "~" H 2650 2300 50  0001 C CNN
	1    2650 2300
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_02x18_Odd_Even Y1
U 1 1 5DC92377
P 5450 3550
F 0 "Y1" H 5500 4567 50  0000 C CNN
F 1 "Arduino_Mega_Bottom_Pins1" H 5500 4476 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x18_P2.54mm_Vertical" H 5450 3550 50  0001 C CNN
F 3 "~" H 5450 3550 50  0001 C CNN
	1    5450 3550
	1    0    0    -1  
$EndComp
Text GLabel 5750 2750 2    50   Input ~ 0
5V
Text GLabel 5250 2750 0    50   Input ~ 0
5V
Text GLabel 5750 4450 2    50   Input ~ 0
GND
Text GLabel 5250 4450 0    50   Input ~ 0
GND
Wire Wire Line
	6150 2850 5750 2850
Wire Wire Line
	6150 800  6150 2850
Wire Wire Line
	6250 1150 6250 2950
Wire Wire Line
	6250 2950 5750 2950
Wire Wire Line
	6350 3050 5750 3050
Wire Wire Line
	6350 1650 6350 3050
Wire Wire Line
	6450 2000 6450 3150
Wire Wire Line
	6450 3150 5750 3150
Wire Wire Line
	6550 3250 5750 3250
Wire Wire Line
	6650 2850 6650 3350
Wire Wire Line
	6650 3350 5750 3350
Wire Wire Line
	6750 3350 6750 3450
Wire Wire Line
	6750 3450 5750 3450
Wire Wire Line
	6850 3700 6850 3550
Wire Wire Line
	6850 3550 5750 3550
Wire Wire Line
	6650 3650 5750 3650
Wire Wire Line
	6650 3650 6650 4200
Wire Wire Line
	6550 3750 5750 3750
Wire Wire Line
	6450 5050 6450 3850
Wire Wire Line
	6450 3850 5750 3850
Wire Wire Line
	6350 5400 6350 3950
Wire Wire Line
	6350 3950 5750 3950
Wire Wire Line
	6250 5900 6250 4050
Wire Wire Line
	6250 4050 5750 4050
Wire Wire Line
	6150 6250 6150 4150
Wire Wire Line
	6150 4150 5750 4150
Text GLabel 1400 1450 0    50   Input ~ 0
Fan
Text GLabel 5250 2850 0    50   Input ~ 0
Fan
$Comp
L Connector_Generic:Conn_01x04 S2
U 1 1 5DDCB599
P 4250 6400
F 0 "S2" H 4330 6392 50  0000 L CNN
F 1 "StepperMotor2" H 4330 6301 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 4250 6400 50  0001 C CNN
F 3 "~" H 4250 6400 50  0001 C CNN
	1    4250 6400
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x04 S1
U 1 1 5DDCF9CA
P 4250 4850
F 0 "S1" H 4330 4842 50  0000 L CNN
F 1 "StepperMotor1" H 4330 4751 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 4250 4850 50  0001 C CNN
F 3 "~" H 4250 4850 50  0001 C CNN
	1    4250 4850
	1    0    0    -1  
$EndComp
Wire Wire Line
	3800 4750 4050 4750
Wire Wire Line
	3800 4850 4050 4850
Wire Wire Line
	3800 4950 4050 4950
Wire Wire Line
	3800 5050 4050 5050
Wire Wire Line
	3800 6300 4050 6300
Wire Wire Line
	3800 6400 4050 6400
Wire Wire Line
	3800 6500 4050 6500
Wire Wire Line
	3800 6600 4050 6600
Text GLabel 2300 5450 0    50   Input ~ 0
StD1En
Text GLabel 2300 5750 0    50   Input ~ 0
StD2En
Text GLabel 2300 5550 0    50   Input ~ 0
StD1St
Text GLabel 2300 5650 0    50   Input ~ 0
StD1Dir
Text GLabel 2300 5850 0    50   Input ~ 0
StD2St
Text GLabel 2300 5950 0    50   Input ~ 0
StD2Dir
Text GLabel 2300 6050 0    50   Input ~ 0
HomeSwitch
Text GLabel 5250 2950 0    50   Input ~ 0
StD1En
Text GLabel 5250 3250 0    50   Input ~ 0
StD2En
Text GLabel 5250 3050 0    50   Input ~ 0
StD1St
Text GLabel 5250 3150 0    50   Input ~ 0
StD1Dir
Text GLabel 5250 3350 0    50   Input ~ 0
StD2St
Text GLabel 5250 3450 0    50   Input ~ 0
StD2Dir
Text GLabel 5250 3550 0    50   Input ~ 0
HomeSwitch
Text GLabel 6800 600  2    50   Input ~ 0
GND
Wire Wire Line
	6350 800  6800 800 
Connection ~ 6800 800 
Wire Wire Line
	6800 800  8550 800 
Wire Wire Line
	6450 1150 6650 1150
$Comp
L Device:R_Small R1
U 1 1 5DF601F7
P 6800 700
F 0 "R1" H 6859 746 50  0000 L CNN
F 1 "10K_Ohm_R" H 6859 655 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 6800 700 50  0001 C CNN
F 3 "~" H 6800 700 50  0001 C CNN
	1    6800 700 
	1    0    0    -1  
$EndComp
Text GLabel 6650 950  2    50   Input ~ 0
GND
$Comp
L Device:R_Small R2
U 1 1 5DF835D5
P 6650 1050
F 0 "R2" H 6709 1096 50  0000 L CNN
F 1 "10K_Ohm_R" H 6709 1005 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 6650 1050 50  0001 C CNN
F 3 "~" H 6650 1050 50  0001 C CNN
	1    6650 1050
	1    0    0    -1  
$EndComp
Wire Wire Line
	8500 1650 6800 1650
Text GLabel 6800 1450 2    50   Input ~ 0
GND
$Comp
L Device:R_Small R3
U 1 1 5DF8D93D
P 6800 1550
F 0 "R3" H 6859 1596 50  0000 L CNN
F 1 "10K_Ohm_R" H 6859 1505 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 6800 1550 50  0001 C CNN
F 3 "~" H 6800 1550 50  0001 C CNN
	1    6800 1550
	1    0    0    -1  
$EndComp
Connection ~ 6650 1150
Wire Wire Line
	6650 1150 7800 1150
Connection ~ 6800 1650
Wire Wire Line
	6800 1650 6550 1650
Wire Wire Line
	6650 2000 6950 2000
Text GLabel 6950 1800 2    50   Input ~ 0
GND
$Comp
L Device:R_Small R4
U 1 1 5DF994C1
P 6950 1900
F 0 "R4" H 7009 1946 50  0000 L CNN
F 1 "10K_Ohm_R" H 7009 1855 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 6950 1900 50  0001 C CNN
F 3 "~" H 6950 1900 50  0001 C CNN
	1    6950 1900
	1    0    0    -1  
$EndComp
Connection ~ 6950 2000
Wire Wire Line
	6950 2000 7750 2000
Wire Wire Line
	8500 2500 7100 2500
Text GLabel 7100 2300 2    50   Input ~ 0
GND
$Comp
L Device:R_Small R5
U 1 1 5DFA4085
P 7100 2400
F 0 "R5" H 7159 2446 50  0000 L CNN
F 1 "10K_Ohm_R" H 7159 2355 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 7100 2400 50  0001 C CNN
F 3 "~" H 7100 2400 50  0001 C CNN
	1    7100 2400
	1    0    0    -1  
$EndComp
Connection ~ 7100 2500
Wire Wire Line
	7100 2500 6750 2500
Wire Wire Line
	6850 2850 7050 2850
Text GLabel 7050 2650 2    50   Input ~ 0
GND
$Comp
L Device:R_Small R6
U 1 1 5DFAF044
P 7050 2750
F 0 "R6" H 7109 2796 50  0000 L CNN
F 1 "10K_Ohm_R" H 7109 2705 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 7050 2750 50  0001 C CNN
F 3 "~" H 7050 2750 50  0001 C CNN
	1    7050 2750
	1    0    0    -1  
$EndComp
Connection ~ 7050 2850
Wire Wire Line
	7050 2850 7750 2850
Wire Wire Line
	8500 3350 7200 3350
Text GLabel 7200 3150 2    50   Input ~ 0
GND
$Comp
L Device:R_Small R7
U 1 1 5DFBB4AE
P 7200 3250
F 0 "R7" H 7259 3296 50  0000 L CNN
F 1 "10K_Ohm_R" H 7259 3205 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 7200 3250 50  0001 C CNN
F 3 "~" H 7200 3250 50  0001 C CNN
	1    7200 3250
	1    0    0    -1  
$EndComp
Connection ~ 7200 3350
Wire Wire Line
	7200 3350 6950 3350
Text GLabel 7350 3500 2    50   Input ~ 0
GND
$Comp
L Device:R_Small R8
U 1 1 5DFC291D
P 7350 3600
F 0 "R8" H 7409 3646 50  0000 L CNN
F 1 "10K_Ohm_R" H 7409 3555 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 7350 3600 50  0001 C CNN
F 3 "~" H 7350 3600 50  0001 C CNN
	1    7350 3600
	1    0    0    -1  
$EndComp
Wire Wire Line
	7050 3700 7350 3700
Connection ~ 7350 3700
Wire Wire Line
	7350 3700 7750 3700
Text GLabel 7100 4000 2    50   Input ~ 0
GND
$Comp
L Device:R_Small R9
U 1 1 5DFD5CE2
P 7100 4100
F 0 "R9" H 7159 4146 50  0000 L CNN
F 1 "10K_Ohm_R" H 7159 4055 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 7100 4100 50  0001 C CNN
F 3 "~" H 7100 4100 50  0001 C CNN
	1    7100 4100
	1    0    0    -1  
$EndComp
Wire Wire Line
	6850 4200 7100 4200
Connection ~ 7100 4200
Wire Wire Line
	7100 4200 8450 4200
Text GLabel 7100 4350 2    50   Input ~ 0
GND
$Comp
L Device:R_Small R10
U 1 1 5DFE1F17
P 7100 4450
F 0 "R10" H 7159 4496 50  0000 L CNN
F 1 "10K_Ohm_R" H 7159 4405 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 7100 4450 50  0001 C CNN
F 3 "~" H 7100 4450 50  0001 C CNN
	1    7100 4450
	1    0    0    -1  
$EndComp
Wire Wire Line
	6750 4550 7100 4550
Connection ~ 7100 4550
Wire Wire Line
	7100 4550 7700 4550
Text GLabel 6900 4850 2    50   Input ~ 0
GND
$Comp
L Device:R_Small R11
U 1 1 5DFEE488
P 6900 4950
F 0 "R11" H 6959 4996 50  0000 L CNN
F 1 "10K_Ohm_R" H 6959 4905 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 6900 4950 50  0001 C CNN
F 3 "~" H 6900 4950 50  0001 C CNN
	1    6900 4950
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 5050 6900 5050
Connection ~ 6900 5050
Wire Wire Line
	6900 5050 8400 5050
Text GLabel 6750 5200 2    50   Input ~ 0
GND
$Comp
L Device:R_Small R12
U 1 1 5DFFB192
P 6750 5300
F 0 "R12" H 6809 5346 50  0000 L CNN
F 1 "10K_Ohm_R" H 6809 5255 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 6750 5300 50  0001 C CNN
F 3 "~" H 6750 5300 50  0001 C CNN
	1    6750 5300
	1    0    0    -1  
$EndComp
Wire Wire Line
	6550 5400 6750 5400
Connection ~ 6750 5400
Wire Wire Line
	6750 5400 7650 5400
Text GLabel 6900 5700 2    50   Input ~ 0
GND
$Comp
L Device:R_Small R13
U 1 1 5E008535
P 6900 5800
F 0 "R13" H 6959 5846 50  0000 L CNN
F 1 "10K_Ohm_R" H 6959 5755 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 6900 5800 50  0001 C CNN
F 3 "~" H 6900 5800 50  0001 C CNN
	1    6900 5800
	1    0    0    -1  
$EndComp
Wire Wire Line
	6450 5900 6900 5900
Connection ~ 6900 5900
Wire Wire Line
	6900 5900 8400 5900
Text GLabel 6750 6050 2    50   Input ~ 0
GND
$Comp
L Device:R_Small R14
U 1 1 5E015A54
P 6750 6150
F 0 "R14" H 6809 6196 50  0000 L CNN
F 1 "10K_Ohm_R" H 6809 6105 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 6750 6150 50  0001 C CNN
F 3 "~" H 6750 6150 50  0001 C CNN
	1    6750 6150
	1    0    0    -1  
$EndComp
Wire Wire Line
	6350 6250 6750 6250
Connection ~ 6750 6250
Wire Wire Line
	6750 6250 7650 6250
$Comp
L Connector_Generic:Conn_01x02 J5
U 1 1 5E032CCA
P 2350 2700
F 0 "J5" H 2268 2917 50  0000 C CNN
F 1 "ArdAnalogTherm" H 2268 2826 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 2350 2700 50  0001 C CNN
F 3 "~" H 2350 2700 50  0001 C CNN
	1    2350 2700
	0    -1   1    0   
$EndComp
Wire Wire Line
	2100 2400 2100 2500
$Comp
L Connector_Generic:Conn_01x02 J4
U 1 1 5E0A79D3
P 1900 2500
F 0 "J4" H 1818 2717 50  0000 C CNN
F 1 "Therm1" H 1818 2626 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 1900 2500 50  0001 C CNN
F 3 "~" H 1900 2500 50  0001 C CNN
	1    1900 2500
	-1   0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x02 J6
U 1 1 5E0F6803
P 2850 2500
F 0 "J6" H 2930 2492 50  0000 L CNN
F 1 "Therm2" H 2930 2401 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 2850 2500 50  0001 C CNN
F 3 "~" H 2850 2500 50  0001 C CNN
	1    2850 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	2450 2500 2650 2500
Connection ~ 2650 2500
Wire Wire Line
	2350 2500 2100 2500
Connection ~ 2100 2500
Text GLabel 2650 2600 3    50   Input ~ 0
GND
Text GLabel 2100 2600 3    50   Input ~ 0
GND
$Comp
L Connector_Generic:Conn_01x02 J3
U 1 1 5E141524
P 1550 7000
F 0 "J3" H 1468 7217 50  0000 C CNN
F 1 "HomeSwitch" H 1468 7126 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical" H 1550 7000 50  0001 C CNN
F 3 "~" H 1550 7000 50  0001 C CNN
	1    1550 7000
	-1   0    0    -1  
$EndComp
$Comp
L Connector:Screw_Terminal_01x02 J2
U 1 1 5E15FADE
P 1100 5650
F 0 "J2" H 1018 5867 50  0000 C CNN
F 1 "12V_Power A97996-ND " H 1018 5776 50  0000 C CNN
F 2 "TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2_1x02_P5.00mm_Horizontal" H 1100 5650 50  0001 C CNN
F 3 "~" H 1100 5650 50  0001 C CNN
	1    1100 5650
	-1   0    0    -1  
$EndComp
Text GLabel 3300 3550 0    50   Input ~ 0
GND
Text GLabel 3800 3550 2    50   Input ~ 0
GND
Text GLabel 3800 3650 2    50   Input ~ 0
Servo5V
Text GLabel 3300 3650 0    50   Input ~ 0
Servo5V
Text GLabel 3300 3750 0    50   Input ~ 0
Servo1
Text GLabel 5250 3750 0    50   Input ~ 0
Servo2
Text GLabel 3800 3750 2    50   Input ~ 0
Servo2
Text GLabel 5250 3650 0    50   Input ~ 0
Servo1
$Comp
L Regulator_Linear:AMS1117-5.0 U4
U 1 1 5DD0B91E
P 1700 3550
F 0 "U4" H 1700 3792 50  0000 C CNN
F 1 "AMS1117-5.0 Servo" H 1700 3701 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-223-3_TabPin2" H 1700 3750 50  0001 C CNN
F 3 "http://www.advanced-monolithic.com/pdf/ds1117.pdf" H 1800 3300 50  0001 C CNN
	1    1700 3550
	1    0    0    -1  
$EndComp
Text GLabel 1400 3550 0    50   Input ~ 0
12V
Text GLabel 2000 3550 2    50   Input ~ 0
Servo5V
Text GLabel 1700 3850 3    50   Input ~ 0
GND
$Comp
L Regulator_Linear:AMS1117-5.0 U3
U 1 1 5DD2CA4F
P 1200 4550
F 0 "U3" H 1200 4792 50  0000 C CNN
F 1 "AMS1117-5.0 RasPi" H 1200 4701 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-223-3_TabPin2" H 1200 4750 50  0001 C CNN
F 3 "http://www.advanced-monolithic.com/pdf/ds1117.pdf" H 1300 4300 50  0001 C CNN
	1    1200 4550
	1    0    0    -1  
$EndComp
Text GLabel 900  4550 0    50   Input ~ 0
12V
Text GLabel 1500 4550 2    50   Input ~ 0
5V
Text GLabel 1200 4850 3    50   Input ~ 0
GND
Text GLabel 5000 1400 0    50   Input ~ 0
GND
Text GLabel 5000 1300 0    50   Input ~ 0
5V
$Comp
L Connector_Generic:Conn_02x03_Odd_Even J1
U 1 1 5DD6D984
P 3500 3650
F 0 "J1" H 3550 3967 50  0000 C CNN
F 1 "RollerServos" H 3550 3876 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x03_P2.54mm_Vertical" H 3500 3650 50  0001 C CNN
F 3 "~" H 3500 3650 50  0001 C CNN
	1    3500 3650
	1    0    0    -1  
$EndComp
Text GLabel 5250 3850 0    50   Input ~ 0
PaperHome
NoConn ~ 5250 3950
NoConn ~ 5250 4050
NoConn ~ 5250 4150
NoConn ~ 5250 4250
NoConn ~ 5250 4350
NoConn ~ 5750 4350
NoConn ~ 5750 4250
Text GLabel 2300 6150 0    50   Input ~ 0
PaperHome
Wire Wire Line
	2300 6050 2350 6050
Wire Wire Line
	2350 6050 2350 7000
Wire Wire Line
	1750 7000 2350 7000
$Comp
L Connector_Generic:Conn_01x04 S3
U 1 1 5DD32497
P 1200 6450
F 0 "S3" H 1280 6442 50  0000 L CNN
F 1 "PaperHome" H 1280 6351 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 1200 6450 50  0001 C CNN
F 3 "~" H 1200 6450 50  0001 C CNN
	1    1200 6450
	-1   0    0    1   
$EndComp
Text GLabel 1400 6550 2    50   Input ~ 0
GND
Text GLabel 1400 6450 2    50   Input ~ 0
GND
Text GLabel 1600 6350 2    50   Input ~ 0
5V
Wire Wire Line
	2300 6150 2300 6250
Wire Wire Line
	2300 6250 1950 6250
$Comp
L Device:R_Small R34
U 1 1 5DD4B703
P 1500 6350
F 0 "R34" V 1304 6350 50  0000 C CNN
F 1 "250_Ohm_Resistor" V 1395 6350 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 1500 6350 50  0001 C CNN
F 3 "~" H 1500 6350 50  0001 C CNN
	1    1500 6350
	0    1    1    0   
$EndComp
$Comp
L Device:R_Small R33
U 1 1 5DD61E98
P 1950 6350
F 0 "R33" H 2009 6396 50  0000 L CNN
F 1 "2.7k_Ohm_Res" H 2009 6305 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 1950 6350 50  0001 C CNN
F 3 "~" H 1950 6350 50  0001 C CNN
	1    1950 6350
	1    0    0    -1  
$EndComp
Wire Wire Line
	1950 6250 1400 6250
Text GLabel 1950 6450 3    50   Input ~ 0
5V
Connection ~ 1950 6250
$Comp
L Transistor_FET:DMN6140L Q15
U 1 1 5DC63D6F
P 2100 1450
F 0 "Q15" H 2306 1496 50  0000 L CNN
F 1 "DMN6140L" H 2306 1405 50  0000 L CNN
F 2 "custom_symbols:SOT-223-edited" H 2300 1375 50  0001 L CIN
F 3 "http://www.diodes.com/assets/Datasheets/DMN6140L.pdf" H 2100 1450 50  0001 L CNN
	1    2100 1450
	1    0    0    -1  
$EndComp
Text GLabel 1800 1250 0    50   Input ~ 0
GND
$Comp
L Device:R_Small R29
U 1 1 5DD8D481
P 1800 1350
F 0 "R29" H 1859 1396 50  0000 L CNN
F 1 "10K_Ohm_R" H 1859 1305 50  0000 L CNN
F 2 "Resistor_SMD:R_0402_1005Metric" H 1800 1350 50  0001 C CNN
F 3 "~" H 1800 1350 50  0001 C CNN
	1    1800 1350
	1    0    0    -1  
$EndComp
Wire Wire Line
	1600 1450 1800 1450
Connection ~ 1800 1450
Wire Wire Line
	1800 1450 1900 1450
$Comp
L Connector_Generic:Conn_02x02_Odd_Even J7
U 1 1 5DDB4E39
P 5200 1300
F 0 "J7" H 5250 1517 50  0000 C CNN
F 1 "Conn_02x02_Odd_Even" H 5250 1426 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x02_P2.54mm_Vertical" H 5200 1300 50  0001 C CNN
F 3 "~" H 5200 1300 50  0001 C CNN
	1    5200 1300
	1    0    0    -1  
$EndComp
Text GLabel 5500 1300 2    50   Input ~ 0
5V
Text GLabel 5500 1400 2    50   Input ~ 0
GND
Wire Wire Line
	8100 1350 10400 1350
Wire Wire Line
	8800 1850 10350 1850
Wire Wire Line
	8850 1000 10450 1000
$EndSCHEMATC
