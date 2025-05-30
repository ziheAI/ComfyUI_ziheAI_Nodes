#@CopyRight By 子禾AI【ziheAI.com】
#🔧 **定制开发服务**  
#- 企业级AI工作流开发  
#- 私有化节点定制  
#- 性能优化服务 
#- 联系微信ziheAI567   

#📧 商务合作：ziheAI567@163.com

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any_type = AnyType("*")
AUTH_OUTPUT = AnyType("AUTH_OUTPUT")