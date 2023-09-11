# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""Pin definitions for the Odroid N2."""

from adafruit_blinka.microcontroller.amlogic.s922x import pin

GPIOX_0 = pin.GPIO476
GPIOX_1 = pin.GPIO477
GPIOX_2 = pin.GPIO478
GPIOX_3 = pin.GPIO479
GPIOX_4 = pin.GPIO480
GPIOX_5 = pin.GPIO481
GPIOX_6 = pin.GPIO482
GPIOX_7 = pin.GPIO483
GPIOX_8 = pin.GPIO484
GPIOX_9 = pin.GPIO485
GPIOX_10 = pin.GPIO486
GPIOX_11 = pin.GPIO487
GPIOX_12 = pin.GPIO488
GPIOX_13 = pin.GPIO489
GPIOX_14 = pin.GPIO490
GPIOX_15 = pin.GPIO491
GPIOX_16 = pin.GPIO492
GPIOX_17 = pin.GPIO493
GPIOX_18 = pin.GPIO494
GPIOX_19 = pin.GPIO495

GPIODV_24 = pin.GPIO493
GPIODV_25 = pin.GPIO494
GPIODV_26 = pin.GPIO474
GPIODV_27 = pin.GPIO475

GPIOA_4 = pin.GPIO464
GPIOA_12 = pin.GPIO472
GPIOA_13 = pin.GPIO473
GPIOA_14 = pin.GPIO474
GPIOA_15 = pin.GPIO475

GPIOA0_0 = pin.GPIO496
GPIOA0_1 = pin.GPIO497
GPIOA0_2 = pin.GPIO498
GPIOA0_3 = pin.GPIO499
GPIOA0_4 = pin.GPIO500
GPIOA0_5 = pin.GPIO501
GPIOA0_6 = pin.GPIO502
GPIOA0_7 = pin.GPIO503
GPIOA0_8 = pin.GPIO504
GPIOA0_9 = pin.GPIO505
GPIOA0_10 = pin.GPIO506
GPIOA0_11 = pin.GPIO507
GPIOA0_12 = pin.GPIO508
GPIOA0_13 = pin.GPIO509
GPIOA0_14 = pin.GPIO510
GPIOA0_15 = pin.GPIO511

for it in pin.i2cPorts:
    globals()["SCL" + str(it[0])] = it[1]
    globals()["SDA" + str(it[0])] = it[2]

SCL = None
SDA = None
# Set second i2c bus as default for backward compatibility.
if len(pin.i2cPorts) > 1:
    SCL = pin.i2cPorts[1][1]
    SDA = pin.i2cPorts[1][2]
elif len(pin.i2cPorts) > 0:
    SCL = pin.i2cPorts[0][1]
    SDA = pin.i2cPorts[0][2]

SCLK = pin.SPI0_SCLK
MOSI = pin.SPI0_MOSI
MISO = pin.SPI0_MISO
SPI_CS0 = pin.GPIO486

D0 = GPIOX_3  # PIN_11
D1 = GPIOX_16  # PIN_12
D2 = GPIOX_4  # PIN_13
D3 = GPIOX_7  # PIN_15
D4 = GPIOX_0  # PIN_16
D5 = GPIOX_1  # PIN_18
D6 = GPIOX_2  # PIN_22
D7 = GPIOA_13  # PIN_7
D8 = GPIOX_17  # PIN_3
D9 = GPIOX_18  # PIN_5
D10 = GPIOX_10  # PIN_24
D11 = GPIOA_4  # PIN_26
D12 = GPIOX_8  # PIN_19
D13 = GPIOX_9  # PIN_21
D14 = GPIOX_11  # PIN_23
D15 = GPIOX_12  # PIN_8
D16 = GPIOX_13  # PIN_10
D21 = GPIOX_14  # PIN_29
D22 = GPIOX_15  # PIN_31
D23 = GPIOX_5  # PIN_33
D24 = GPIOX_6  # PIN_35
D26 = GPIOA_12  # PIN_32
D27 = GPIOX_19  # PIN_36
D30 = GPIOA_14  # PIN_27
D31 = GPIOA_15  # PIN_28
