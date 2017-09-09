from castle.command import Command
from castle.context.merger import ContextMerger
from castle.exceptions import InvalidParametersError


class CommandsTrack(object):
    def __init__(self, context):
        self.context_merger = ContextMerger(context)

    def build(self, options):
        event = options.get('event')
        if event is None or event == '':
            raise InvalidParametersError

        if 'active' in options.get('context', dict()):
            if not isinstance(options.get('context').get('active'), bool):
                del options['context']['active']

        args = {
            'event': event,
            'context': self.build_context(options.get('context', dict()))
        }

        if 'user_id' in options:
            args['user_id'] = options['user_id']

        if 'properties' in options:
            args['properties'] = options['properties']

        if 'traits' in options:
            args['traits'] = options['traits']

        return Command(method='post', endpoint='track', data=args)

    def build_context(self, context):
        return self.context_merger.call(context or {})
