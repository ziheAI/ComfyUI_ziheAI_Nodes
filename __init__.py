#@CopyRight By 子禾AI【ziheAI.com】
#🔧 **定制开发服务**  
#- 企业级AI工作流开发  
#- 私有化节点定制  
#- 性能优化服务 
#- 联系微信ziheAI567   

#📧 商务合作：ziheAI567@163.com


from .nodes.auth_node import ZiheAuthNode
from .nodes.random_node import RandomDateNode
from .nodes.pipeline_node import DataPipeline
from .nodes.stringdel_node import StringDel
from .nodes.imgnameext_node import ImgNameExt
from .nodes.baidutranslate_node import  BaiduTranslate_API

NODE_CLASS_MAPPINGS = {
    "ZiheAuthNode": ZiheAuthNode,
    "RandomDateNode": RandomDateNode,
    "DataPipeline": DataPipeline,
    "StringDel": StringDel,
    "ImgNameExt": ImgNameExt,
    "BaiduTranslate_API": BaiduTranslate_API
    
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ZiheAuthNode": "🔑 验证免费(ziheAI.com)微信ziheAI567",
    "RandomDateNode": "🔄 日期+随机字符串",
    "DataPipeline": "⚙️ 数据处理管道",
    "StringDel": "📝 删除字符串",
    "ImgNameExt": "📷 图片名称提取",
    "BaiduTranslate_API": "🌎 百度翻译API"
}

print("                                                                     ")
print("                                                                     ")
print("                                                                     ")
print("███████╗██╗██╗  ██╗███████╗ █████╗ ██╗    ██████╗ ██████╗ ███╗   ███╗")
print("╚══███╔╝██║██║  ██║██╔════╝██╔══██╗██║   ██╔════╝██╔═══██╗████╗ ████║")
print("  ███╔╝ ██║███████║█████╗  ███████║██║   ██║     ██║   ██║██╔████╔██║")
print(" ███╔╝  ██║██╔══██║██╔══╝  ██╔══██║██║   ██║     ██║   ██║██║╚██╔╝██║")
print("███████╗██║██║  ██║███████╗██║  ██║██║██╗╚██████╗╚██████╔╝██║ ╚═╝ ██║")
print("╚══════╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝")
print("                                                                     ")
print(f"\33[93m》===>====>========>\33[34m[ziheAI-nodes]\33[32m 插件初始化完成\33[0m<\33[93m========<====<===《\33[0m")
print("                                                                     ")
print("                                                                     ")
print("                                                                     ")