#@CopyRight By 子禾AI【ziheAI.com】
#🔧 **定制开发服务**  
#- 企业级AI工作流开发  
#- 私有化节点定制  
#- 性能优化服务 
#- 联系微信ziheAI567   

#📧 商务合作：ziheAI567@163.com

import os
from ..base.base_node import BaseNode
from ..base.types import AUTH_OUTPUT

class ImgNameExt(BaseNode):
    """
    🖼️ 纯净文件名提取节点
    功能：专注从文件路径提取无扩展名的文件名
    输入类型：STRING (文件路径)
    输出类型：STRING (纯文件名)
    """
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("img_name",)
    

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_path": ("AUTH_OUTPUT", {
                    "forceInput": True,
                    "multiline": False,
                    "dynamicPrompts": False
                })
            }
        }

    def func(self, file_path):
        try:
            # 跨平台路径处理
            base_name = os.path.basename(file_path)
            # 处理多重扩展名（例如：.tar.gz）
            file_name = base_name.rsplit('.', 1)[0]
            return (file_name,)
        except Exception as e:
            print(f"❌ 路径解析错误: {str(e)}")
            return ("",)
