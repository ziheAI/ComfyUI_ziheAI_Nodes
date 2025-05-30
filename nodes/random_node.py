#@CopyRight By 子禾AI【ziheAI.com】
#严禁在未经授权情况下用于任何商用行为
#🔧 **定制开发服务**  
#- 企业级AI工作流开发  
#- 私有化节点定制  
#- 性能优化服务 
#- 联系微信ziheAI567   

#📧 商务合作：ziheAI567@163.com

import datetime
import random
import string
from ..base.base_node import BaseNode
from ..base.types import any_type
from ..base.types import AUTH_OUTPUT

class RandomDateNode(BaseNode):
    RETURN_TYPES = (any_type, "STRING")
    RETURN_NAMES = ("passthrough", "random_str")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_data": (AUTH_OUTPUT, {"default": None})
            }
        }

    def func(self, input_data, **kwargs):
        current_date = datetime.datetime.now().strftime("%Y%m%d")
        random_chars = ''.join(random.choices(
            string.ascii_letters + string.digits, 
            k=8
        ))
        random_str = f"{current_date}_{random_chars}"
        return (input_data, random_str)
