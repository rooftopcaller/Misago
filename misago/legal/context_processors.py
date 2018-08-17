from django.urls import reverse

from .models import Agreement
from .utils import get_required_user_agreement, get_parsed_content


# fixme: rename this context processor to more suitable name
def legal_links(request):
    agreements = Agreement.objects.get_agreements()

    legal_context = {}

    terms_of_service = agreements.get(Agreement.TYPE_TOS)
    if terms_of_service:
        if terms_of_service['link']:
            legal_context['TERMS_OF_SERVICE_URL'] = terms_of_service['link']
        elif terms_of_service['text']:
            legal_context['TERMS_OF_SERVICE_URL'] = reverse('misago:terms-of-service')

    privacy_policy = agreements.get(Agreement.TYPE_PRIVACY)
    if privacy_policy:
        if privacy_policy['link']:
            legal_context['PRIVACY_POLICY_URL'] = privacy_policy['link']
        elif privacy_policy['text']:
            legal_context['PRIVACY_POLICY_URL'] = reverse('misago:privacy-policy')

    if legal_context:
        request.frontend_context.update(legal_context)

    required_agreement = get_required_user_agreement(request.user, agreements)
    if required_agreement:
        request.frontend_context['REQUIRED_AGREEMENT_ID'] = required_agreement.id

        legal_context['misago_agreement'] = {
            'title': required_agreement.get_final_title(),
            'link': required_agreement.link,
            'content': get_parsed_content(request, required_agreement)
        }
    else:
        legal_context['misago_agreement'] = None

    return legal_context
