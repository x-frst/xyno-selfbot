from cfg.cfg import get_value

def check_usage(ctx):
    if str(get_value('global_usage')) == 'True':
        return True
    elif str(get_value('global_usage')) == 'False':
        if ctx.author.id == int(get_value('owner')):
            return True
        else:
            return False