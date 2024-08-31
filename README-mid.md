# Mid level Operations

## stream tags

Runs parallel to the main data stream. stream tag, 被一个block的work function添加, 从那里开始，flow donwstream, 和一个特定的采样传播，直到它到达一个sink, 或被另一个模块截取。
key:value pair. PMT, Polymorphic Types, key是一个PMT symbol符号, 可以处理任意格式的数据类型。

scrid, 标明生成这个tag的模块， block's alias.

GNU Radio是一个streaming 系统，无法在block之间传递数据。缺乏control, metadata. 使用现存的message passing interface, 允许模块注册到消息in the flowgraph. Message passing. 消息传递是异步的, 

gr::block, absolute item numbers, 每一个block's work function, 都有一个buffer in the data stream, 0~N-1, relative offset into the data stream. 

```c
unsigned long int nitems_read(unsigned int which_input);
    nitems_written(unsigned int which_output);
gr::block::add_item_tag();
gr::tag_t,
void add_item_tag(); // 添加tag,
```
a tag 定义为:
* offset, absolute item time in the data stream,
* key: the PMT symbol identifying the type of tag,
* value, the PMT holding the data of the tag,
* scrid, 可选的, PMTsymbol identifying the block , the creator

python代码
```python
add_item_tag()

```
python block,

获取tag from a stream, 

```c
void get_tags_in_range();

```

### tag的传播

3种策略:
- all-to-all, 输入到Input传送到所有的output, 默认
- one-to-one, 
- Dont, 不传播,

```c
void set_tag_propagation_polic();
```

GNU Radio scheduler.

使用Tags,
Metadata source, Metadata sink,

tags对scheduler是没有影响的。越来越像FFMPEG了。少用, USRP source， 生成一个时间tag, 

## Polymorphic Types, PMTs,

作为carrier of data, stream tags, message passing, 




