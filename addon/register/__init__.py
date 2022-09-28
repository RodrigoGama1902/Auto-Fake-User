

def register_addon():
    
    from ..handlers import register_handlers
    register_handlers()
    
    from ..property import register_props
    register_props()
    
    from ..panels import register_panels
    register_panels()
    
def unregister_addon():
    
    from ..handlers import unregister_handlers
    unregister_handlers()
    
    from ..property import unregister_props
    unregister_props()
    
    from ..panels import unregister_panels
    unregister_panels()
    
