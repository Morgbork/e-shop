from .signals import object_viewed_signal

class ObjectViewedMixin(object):
    def get_context_data(self, *args, **kwargs):
        content = super(ObjectViewedMixin, self).get_context_data(*args, **kwargs)
        request=self.request
        instance = context.get('object')
        if instance:
            object_viewed_signal.send(product.__class__, instance=product, request=request)