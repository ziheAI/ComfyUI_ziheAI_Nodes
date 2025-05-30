#@CopyRight By 子禾AI【ziheAI.com】
#🔧 **定制开发服务**  
#- 企业级AI工作流开发  
#- 私有化节点定制  
#- 性能优化服务 
#- 联系微信ziheAI567   

#📧 商务合作：ziheAI567@163.com

import os
from ..base.base_node import BaseNode

class StringDel(BaseNode):
    """Delete specified substring/pattern from string."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": ("STRING", {"forceInput": True}),
                "target": ("STRING", {"default": ""}),  # 改名 old -> target 更符合删除语义
                "use_regex": ("BOOLEAN", {"default": False}),
            }
        }

    FUNCTION = "delete_str"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)

    def delete_str(self, string: str, target: str, use_regex: bool):

        if not target:  # 空删除目标直接返回原字符串
            return (string,)

        try:
            if use_regex:
                string = re.sub(target, "", string)
            else:
                string = string.replace(target, "")
        except re.error as e:
            raise ValueError(f"Regex error: {e}") from e

        return (string,)