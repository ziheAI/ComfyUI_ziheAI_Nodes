#@CopyRight By 子禾AI【ziheAI.com】
#严禁在未经授权情况下用于任何商用行为
#🔧 **定制开发服务**  
#- 企业级AI工作流开发  
#- 私有化节点定制  
#- 性能优化服务 
#- 联系微信ziheAI567   

#📧 商务合作：ziheAI567@163.com

from ..base.base_node import BaseNode
from ..base.types import any_type

class DataPipeline(BaseNode):
    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ("*",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {"anything": (any_type, {"default": None})}
        }

    def func(self, anything=None, **kwargs):
        return (anything,)
