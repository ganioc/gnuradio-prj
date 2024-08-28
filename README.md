# How to use GNURadio

## 参考书籍

- Software Defined Radio for Engineers
- Thierry Turletti's software radio resource page
- Software radio A Modern Approach to Radio Engineering
- Putting FPGAs to Work for software Radio Handbook 12th Edition
- SDR platform enables reconfigurable direction finding system
- RF and digital signal processing for Software-Defined Radio: A Multi-Mode Approach, Rouphael
- Learn SDR with Prof Jason, Youtube videos,
- Quadrature Signals: Complex , But not complicated
- MIT OpenCourseWare Lecture, Divide and Conquer: FFT
- PySDR: A guide to SDR and DSP using Python,
- Practical Signal Processing, Mark Owen,
- Understanding Digital Signal Processing, Richard Lyons,
- Digital signal processing, A practical Approach, Ifeachor and Jervis,
- Discrete-Time Signal Processing, Alan V.
- DSPLinks,
- MIT Digital Signal Processing online course,
- Signal Processing for Communications, Paolo Prandoni, Martin Vetterli,
- Think DSP by Allen Downey,
  
### Digital Comms

- MIT 6.450 Principle of Digital Communications, full course available on OCW,
- Principles of Digital Communications , Professor Gallager
- Digital Signal Processing in Communication Systems, Marvin E. Frerking
- Digital Communications, Fundamentals an Applications, 2nd ed.
- Digital and Analog Communication Systems, Leon W. Couch II,
- Digital Communications 3rd, John Proakis,
- Fundamentals of Wireless Communication, David Tse , Pramod Viswanathan,
- Multirate Signal Processing for Communication Systems
- Wireless Digital Communications: Design and Theory
- Communication Systems Design Using DSP Algorithms: With laboratory Experiments for the TMS320C6701 and TMS320C6711
- complextoreal.com's Communications Tutorials
- Telecommunication Breakdown Concepts of Communication Transmitted via Software-Defined Radio, Richard Johnson, William A. Sethares
- A Foundation in Digital Communication, Amos Lapidoth,
- Digital Communication, 3rd Edition,
- Wireless Communications From the Groud Up, An SDR Perspective, Qasim Chaudhari,

#### Radio and RF Design

- The Science of Radio, Paul J Nahin,
- The electronics of Radio, David B. Rutledge
- RF Circuit Design, Chris Bowick,
- The Darker Side, Robert Lacoste,
- Experimental Methods in RF Design, Wes Hayward, Rick Campbell, Bob Larkin,
- The ARRL Handbook,

#### Electronics

- The Art of Electronics, Horowitz and Hill
- IC Op-Amp Cookbook, Walter Jung,
- Intuitive Operational Amplifiers, Thomas Frederiksen
- Analog Electronics with Op Amps, Peyton Walsh

#### C++

- C++ Primer
- The C++ Standard Library, a Tutorial and Reference, Nicolai M. Josuttis,
- boost.org C++ libraries,
- Effective C++ Libraries,
- Large-scale c++ software design, John Lakos
- Thinking in C++,

#### Python

- python online tutorial, docs.python.org/tutorial
- Python3 online docs
- PySDR: A Guid to SDR and DSP using Python
- Python Essential Reference, 2nd David M. Beazley
- How to Think Like a Computer Scientist: Learning with Python,
- Python Applications for Digital Design and Signal Processing, Dan Boschen ,

#### Verilog

- FPGA Prototyping by Verilog Examples
- Verilog HDL Synthesis: A Practical Primer, J. Bhasker,

#### Amateur Radio Licensing

- Now You're Talking!, ARRL, 35个问题

## 简介

Signal processing blocks, 实现software radios, low cost external RF hardware, 来生成软件无线电。

使用软件来进行需要的信号处理, 而不是使用专用的硬件电路。好处是软件可以简单替换，硬件可以用来生成各种各样的radios, 满足不同的传输标准。

GNU Radio执行所有的信号处理。你可以使用它来编写应用，接收digital streams, 或者将数据推送。使用硬件来发送。

GNU radio有filters, channel codes, synchronisation elements, equalizers, demodulators, vocoders, decoders, blocks。 将这些block连接到一起，数据如何从一个模块流向另一个模块。扩展GNU Radio非常容易。

只能处理数字数据。复数基带采样，是接收机的输入数据类型和输出数据类型。模拟硬件可以用来将信号移到需要的中心射频频率。任何数据类型都可以从模块间传输, bits, bytes, vectors, bursts, 或complex data tytes, 复数据类型。

GNU Radio主要用Python编程语言。与性能critical, 关键的信号处理路径是用C++编写的，processor floating point extensions. 开发者可以实现实时，高吞吐量的无线系统。简单易用, 快速应用开发环境。

## 编程方法

GNU Radio Companion, 一个GUI界面，类似于Simulink, 可以使用signal processing applications, 拖放的方式。
如果要扩展GNU Radio, 必须编写代码。Python, c++。

## 第三方库

- BBN 802.11, 使用bootstrap/configure/make  非初学者使用
- MRFM, Magnetic Resonance Force Microscopy, On FPGA side, 2-stage biquad filter with 24 bit data path and filter coefficients, input multiplexer and adder, host side, python, scipy code, transfer functions, ratios of polynomials with floating point coefficients, into cascaded biquad stages with scaled integer coefficients
- GNR Radio Companion files, grc-examples,
- GR Bluetooth stack
- Jitter, GNU Ionospheric Tomography Receiver
- gr-baz, RTL2832 drivers, eye diagrams and other stuffs

## 安装

## 文档, Documentation

### 用户文档

### 开发者文档

C++ API Reference,

## Tutorials

GNU Radio Academy,

### 第一个flowchart, 流程图

GRC, GnuRadio Companion,

options block,

<<< Welcome to GNU Radio Companion 3.10.7.0 >>>
Block paths:  /usr/share/gnuradio/grc/blocks

#### Browse blocks, blocks

- Waveform Generators
  - Signal Source
  - Random Source,
  - Glfsr source,
- Misc
  - throttle, 使输出不会超过sample_rate,flow control,
  - Python Block,就是embedded python block,
  - Virtual Sink,
  - Vector source,
- Instrumentation
  - QT
    - QT GUI Frequency Sink, 频域,
    - QT GUI Time Sink, 时域,
- GUI Widgets
  - QT
    - QT GUI Range
    - QT GUI Chooser
- Type converter
  - char to float
- Byte Operators
  - Pack K Bits,
- Stream Operators
  - Stream to vector
  - Repeat, 
- Variable
  - parameter, 
- Message Tools
  - Message Debug, 打印调试信息
- Math Operation
  - multiply const, 与常数相乘
  - add const,
- Filter
  - Low pass filter




#### Python Variables in GRC

Python 变量, 使用Python数据类型来表示变量。number, 可以是浮点数或者整数。float(), int(),
list,
tuple,

List Comprehension, 在变量里面写一个函数, function, 

float: orange 橙色
int:   green 绿色
string: purple 紫色

GUI range, 在运行时修改flowgraph的变量

### Signal Data Types:

模块的输入，输出端口, 都带有一个数据类型, 用颜色来标记。

Converting Data Types,
Random Sources, 
Pack bits into a byte, 
Stream, 1 sample each time instance,
Vectors,multi 采样，each time instance,

Hier Blocks and Parameters,
    生成一个复合模块,block, 

parameter : accept a value from external source
variable: exists internally to the hier block

放在 ./.grc_gnuradio/目录下, .py, .block.yml,

### Create Block

生成Embedded Python Block, 来作为一个signal processing block, in GNU Radio.

OOT, Out-of-tree, module, 可以在flowgraph里安装使用。
在python代码里, numpy as np, gnuradio import gr,
    np.complex64就是GNU Radio Complex Float 32,

### Python Block with Vectors,

stream, input, output, 可以用port number, sample index来索引。input_items[portIndex][sampleIndex]
input_items[portIndex][vectorIndex][sampleIndex]

virtual sink, virtual source, 似乎是连接在一起的
注意tab, space的问题,

### Python Block Message Passing,

Messages是一种异步的方式，在模块间发送信息的。用于传送控制信息，保持状态，提供某种形式的非数据的反馈信息。

消息的几个特性:
1. 当消息到达时，并不是基于采样时钟同步的
2. 消息不与某一采样联系，如同tag
3. 消息的输入和输出端口不与GRC连接
4. 消息端口使用PMT, Polymorphic Type, 多态类型

根据接收到的消息，改变work()函数里面的模块的行为;

### Python Block Tags

检测input signal crosses the threshold, 写一个tag, 在另一个模块读取这个tag, 更新输出，tag发生的时间, last detection,

用于在采样信号上加标签tag, 同步的方式。当下行的模块需要知道接收机将哪些样本调到了新频率，或者在某些采样上附加timestamp.

标签可以在stream，或者vector上，Complex Float32, Float 32, Byte, 和所有其它的数据格式。

absolute index,
relative index,

### DSP Blocks,

LPF block,
Impulse Response of a Filter,

Frequency Xlating FIR Filter, 


## Use with HackRF

### As a signal generator



### As a spectrum analyzer












