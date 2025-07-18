from django.core.cache import cache

def banner_settings(request):
    """Context processor to make banner settings available in all templates"""
    try:
        # Get banner settings from cache instead of session
        banner_enabled = cache.get('banner_enabled', False)
        banner_text = cache.get('banner_text', '')
        banner_type = cache.get('banner_type', 'info')
        
        # Validate banner type
        valid_types = ['info', 'warning', 'success', 'danger']
        if banner_type not in valid_types:
            banner_type = 'info'
        
        return {
            'banner_enabled': bool(banner_enabled),
            'banner_text': str(banner_text),
            'banner_type': str(banner_type),
        }
    except Exception:
        # Return default values if there's any error
        return {
            'banner_enabled': False,
            'banner_text': '',
            'banner_type': 'info',
        } 