"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        

    def work(self, input_items, output_items):
        for indx, sample in enumerate(input_items[0]): # enumerate through the input 
        # samples in port in0
            if np.random.rand() > 0.95: # 5% chance, this sample is chosen,
                key = pmt.intern("example_key")
                value = pmt.intern("example_value")
                self.add_item_tag(0, # write to output port 0
                        self.nitems_written(0) + indx, # index of the tag in absolute terms
                        key,
                        value
                
                )
                # (self.nitems_written(0)+indx) shi current sample in absolute time
        
        
        output_items[0][:] = input_items[0]
        return len(output_items[0])
        
        
        
