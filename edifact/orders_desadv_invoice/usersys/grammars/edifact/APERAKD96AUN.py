from bots.botsconfig import *
from recordsD96AUN import recorddefs
from edifact import syntax

structure=    [
{ID:'UNH',MIN:1,MAX:1,LEVEL:[
{ID:'BGM',MIN:1,MAX:1},	
{ID:'DTM',MIN:0,MAX:9},	
{ID:'FTX',MIN:0,MAX:9},	
{ID:'CNT',MIN:0,MAX:9},	
{ID:'RFF',MIN:0,MAX:10,
    LEVEL:[
    {ID:'DTM',MIN:0,MAX:9},
    ]},        
{ID:'NAD',MIN:0,MAX:9,LEVEL:[	
    {ID:'CTA',MIN:0,MAX:9},	
    {ID:'COM',MIN:0,MAX:9},
    ]},            
{ID:'ERC',MIN:0,MAX:999,LEVEL:[	
    {ID:'FTX',MIN:0,MAX:1},	
    {ID:'RFF',MIN:0,MAX:1,LEVEL:[	
        {ID:'FTX',MIN:0,MAX:9},
        ]},
    ]},            
{ID:'UNT',MIN:1,MAX:1},	
]
}
]