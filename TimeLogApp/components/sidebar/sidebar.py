from django_components import component

@component.register("sidebar")
class Table(component.Component):
        template_name="sidebar/sidebar.html"  
        
        def get_context_data(self):
                return{
                    
                    }
        class Media:
            css = {
                'all': ['css/sidebar.css']
            }