


class Paginator():
    
    def __init__(self, paginator, request, delta=5, page_variable='page'):
        """
        paginator = django.core.paginator.Paginator object.
        request = django.http.HttpRequest object.
        delta = numbers of links before and after current page links.
        page_variable = the name of query parameter which specifies current page number.
        """
        
        self.paginator = paginator
        self.request = request
        self.delta = delta
        self.page_variable = page_variable
        self.page_list = []
        
        current_page = request.GET.get(self.page_variable, 1)
        max_page = paginator.num_pages
        
        query_dict = request.GET.copy()
        for i in (current_page - self.delta, current_page + self.delta):
            if i < 1 or i > max_page:
                continue
            
            query_dict[self.page_variable] = i
            self.page_list.append( {'page': i, 'url': query_dict.urlencode()} )
    
    def __iter__(self):
        return self.page_list
    
