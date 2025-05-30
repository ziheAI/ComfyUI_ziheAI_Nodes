#@CopyRight By 子禾AI【ziheAI.com】
#🔧 **定制开发服务**  
#- 企业级AI工作流开发  
#- 私有化节点定制  
#- 性能优化服务 
#- 联系微信ziheAI567   

#📧 商务合作：ziheAI567@163.com

from ..base.base_node import BaseNode
from ..base.types import any_type
from ..base.types import AUTH_OUTPUT

class ZiheAuthNode(BaseNode):
    RETURN_TYPES = (AUTH_OUTPUT, "STRING")
    RETURN_NAMES = ("output", "status")

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "cardCode": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "dynamicPrompts": False
                })
            },
            "optional": {
                "passthrough": (any_type, {"default": None})
            }
        }

    def func(self, cardCode, passthrough=None, **kwargs):
        cleaned_code = cardCode.strip()
        if cleaned_code != "ziheAI.com":
            print(f"【验证失败,请+开发者微信ziheAI567免费获取口令!!!】")
            return (None, "❌验证失败❌")
        return (passthrough, "✅验证成功✅")
