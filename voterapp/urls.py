# # working code

# from django.urls import path
# from .views import UserListCreate, UserRetrieveUpdateDestroy
# from .views import UserLogin
# from . views import upload_file
# from .views import get_voters
# from .views import TownList
# from .views import BoothList
# from .views import PanchayatSamitiListCreate, PanchayatSamitiRetrieveUpdateDestroy
# from .views import ZPlistCreate, ZPRetrieveUpdateDestroy
# from .views import VidhansabhaListCreate, VidhansabhaRetriveUpdateDestroy
# from .views import StateListCreate, StateRetriveUpdateDestroy
# from .views import VoterlistListCreate, VoterlistRetrieveUpdateDestroy
# from .views import get_voters_by_booth
# from .views import GetVoterByCastView
# from .views import FirmLogin
# from .views import FirmCreate
# from .views import ReligionListCreate
# from .views import ReligionRetriveUpdateDestroy
# from .views import Favour_non_favourListCreate
# from .views import Favour_non_favourRetriveUpdateDestroy 



# urlpatterns = [
#     path('register/', UserListCreate.as_view(), name='user-list'),
#     path('register/<int:pk>/', UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
#     path('login/', UserLogin.as_view(), name='user-login'),  
#     path('upload/', upload_file, name='upload_file'),
#     path('get_voters/', get_voters, name='get_voters'),
#     path('voters/', VoterlistListCreate.as_view(), name='voter-list-create'),
#     path('voters/<int:voter_id>/', VoterlistRetrieveUpdateDestroy.as_view(), name='voter-detail'),
#     path('towns/', TownList.as_view(), name='town-list'),
#     path('booths/', BoothList.as_view(), name='booth-list'),
#     path('panchayat_samitis/', PanchayatSamitiListCreate.as_view(), name='panchayat-samiti-list-create'),
#     path('panchayat_samitis/<int:pk>/', PanchayatSamitiRetrieveUpdateDestroy.as_view(), name='panchayat-samiti-detail'),
#     path('zps/', ZPlistCreate.as_view(),name = 'zp-list-create'),
#     path('zps/<int:pk>/', ZPRetrieveUpdateDestroy.as_view(), name='zp-details'),
#     path('vidhansabhas/', VidhansabhaListCreate.as_view(), name = 'vidhansabha-list-create'),
#     path('vidhansabha/<int:pk>/',VidhansabhaRetriveUpdateDestroy.as_view(), name = 'vidhansabha-details'),
#     path('states/', StateListCreate.as_view(), name = 'state-list-create'),
#     path('states/<int:pk>/',StateRetriveUpdateDestroy.as_view(), name = 'state-details'),
#     path('get_voters_by_booth/<int:booth_id>/', get_voters_by_booth, name='get_voters_by_booth'),
#     path('voters_by_cast/<str:voter_cast>/', GetVoterByCastView.as_view(), name='voter-by-cast'),
#     path('firm_login/', FirmLogin.as_view(), name='firm-login'),
#     path('firm_register/', FirmCreate.as_view(), name='user-list'),
#     path('religion/', ReligionListCreate.as_view(), name='religion-list'),
#     path('religion/<int:pk>/', ReligionRetriveUpdateDestroy.as_view(), name='religion-detail'),
#     path('favour/', Favour_non_favourListCreate.as_view(), name='Favour_non_favour-list'),
#     path('favour/<int:pk>/', Favour_non_favourRetriveUpdateDestroy.as_view(), name='Favour_non_favour-detail'),


# ]


from django.urls import path
from .views import UserListCreate, UserDetail
from .views import UserLogin, UserLogout
from .views import upload_file
from .views import get_voters
from .views import TownList
from .views import BoothList
from .views import PanchayatSamitiListCreate, PanchayatSamitiRetrieveUpdateDestroy
from .views import ZPListCreate, ZPRetrieveUpdateDestroy
from .views import VidhansabhaListCreate, VidhansabhaRetriveUpdateDestroy
from .views import StateListCreate, StateRetriveUpdateDestroy
from .views import VoterlistListCreate, VoterlistRetrieveUpdateDestroy
from .views import get_voters_by_booth
from .views import GetVoterByCastView
from .views import PoliticianLoginView
from .views import PoliticianCreate
from .views import ReligionListCreate
from .views import ReligionRetriveUpdateDestroy
# from .views import Favour_non_favourListCreate
from .views import Favour_non_favourRetriveUpdateDestroy
from .views import Town_userLogin
from .views import Town_userCreate
from .views import get_town_voter_list
from .views import get_taluka_voter_list
from .views import VotersByConstituencyView
from .views import MaritalStatusRetrieveUpdateDestroy
from .views import get_voters_by_constituency
from .views import get_voters_by_userwise
from .views import EditedVoterlistList
from .views import EditedVoterlistByDate
from .views import VoterlistByTown
from .views import VoterCountView
from .views import VoterCountByBoothView
from .views import BoothListByTown
from .views import total_voters
from .views import BoothCountView, TownCountView
from .views import get_all_voters
from .views import VoterlistByReligion,ReligionListView
from .views import VoterlistByReligionView
from .views import UserBoothDeleteView
from .views import TownUserTownDeleteView
from .views import update_town_panchayat
from .views import get_panchayat_samiti_circle
from .views import update_panchayat_circle


# admin pannel
from django.urls import path, include



urlpatterns = [
    path('register_user/', UserListCreate.as_view(), name='user-list-create'),
    path('register_user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('userboothdelete/<int:user_booth_user_id>/', UserBoothDeleteView.as_view(), name='user_booth_delete'),
    path('townusertowndeleteView/<int:user_town_user_id>/', TownUserTownDeleteView.as_view(), name='user_town_delete'),
    
    path('user_login/', UserLogin.as_view(), name='user-login'), 
    path('user_logout/', UserLogout.as_view(), name='logout'),

    path('upload/', upload_file, name='upload_file'),
    path('get_voters/', get_voters, name='get_voters'),
    path('get_voters/<int:booth_id>/', get_voters, name='get_voters'),                          # getting error for fetch perticular voter 
    path('towns/', TownList.as_view(), name='town-list'),
    path('booths/', BoothList.as_view(), name='booth-list'),
    path('booths/<int:booth_id>/', BoothList.as_view(), name='booth-detail'),
    path('panchayat_samitis/', PanchayatSamitiListCreate.as_view(), name='panchayat-samiti-list-create'),
    path('panchayat_samitis/<int:pk>/', PanchayatSamitiRetrieveUpdateDestroy.as_view(), name='panchayat-samiti-detail'),
    path('zps/', ZPListCreate.as_view(),name = 'zp-list-create'),
    path('zps/<int:pk>/', ZPRetrieveUpdateDestroy.as_view(), name='zp-details'),
    path('vidhansabhas/', VidhansabhaListCreate.as_view(), name = 'vidhansabha-list-create'),
    path('vidhansabha/<int:pk>/',VidhansabhaRetriveUpdateDestroy.as_view(), name = 'vidhansabha-details'),
    path('states/', StateListCreate.as_view(), name = 'state-list-create'),
    path('states/<int:pk>/',StateRetriveUpdateDestroy.as_view(), name = 'state-details'),
    path('voters/', VoterlistListCreate.as_view(), name='voter-list-create'),
    path('voters/<int:voter_id>/', VoterlistRetrieveUpdateDestroy.as_view(), name='voter-detail'),
    path('get_voters_by_booth/<int:booth_id>/', get_voters_by_booth, name='get_voters_by_booth'),
    path('get_voters_by_booth/<int:booth_id>/<int:voter_id>/', get_voters, name='voter_detail'),
    path('voters_by_cast/<str:voter_cast>/', GetVoterByCastView.as_view(), name='voter-by-cast'),
    path('politician_register/', PoliticianCreate.as_view(), name='Politician-list'), 
    path('politician_login/', PoliticianLoginView.as_view(), name='politician-login'),
    path('religion/', ReligionListCreate.as_view(), name='religion-list'),
    path('religion/<int:pk>/', ReligionRetriveUpdateDestroy.as_view(), name='religion-detail'),
    # path('favour/', Favour_non_favourListCreate.as_view(), name='Favour_non_favour-list'),
    path('favour/<int:pk>/', Favour_non_favourRetriveUpdateDestroy.as_view(), name='Favour_non_favour-detail'),
    path('town_user_login/', Town_userLogin.as_view(), name='town_user-login'),
    path('town_user_register/', Town_userCreate.as_view(), name='town_user-list'), 
    path('get_town_voter_list/<int:town_user_town_id>/', get_town_voter_list, name='get_voters_by_town_user'),
    path('get_taluka_voter_list/<int:politician_taluka_id>/', get_taluka_voter_list, name='get_voters_by_town_user'),
    path('constituency/<int:constituency_id>/', VotersByConstituencyView.as_view(), name='voters-by-constituency'),
    path('get_voters_by_booth/<int:booth_id>/<int:voter_id>/', get_voters_by_booth, name='update_voter'),
    path('marital_status/<int:pk>/', MaritalStatusRetrieveUpdateDestroy.as_view(), name='marital-status-detail'),
    path('get_voters_by_constituency/<int:constituency_id>/', get_voters_by_constituency, name='constituency_voter_list'),
    path('get_voters_by_user_wise/<int:user_booth_user_id>/', get_voters_by_userwise, name='get_voters_by_userwise'),
    path('edited_voters/', EditedVoterlistList.as_view(), name='edited-voter-list'), 
    path('edited_voters/<int:user_id>/', EditedVoterlistList.as_view(), name='edited-voter-list-by-user'),
    path('edited_voters_date/<str:date>/', EditedVoterlistByDate.as_view(), name='edited-voter-list-by-date'),
    path('town_wise_voter_list/<int:town_id>/', VoterlistByTown.as_view(), name='voterlist-by-town'),
    path('voter_count/', VoterCountView.as_view(), name='voter-count'),
    path('votercountbyboothview/<int:voter_booth_id>/', VoterCountByBoothView, name='votercountbyboothview'),
    path('booths_by_town/<int:town_id>/', BoothListByTown.as_view(), name='boothlist-by-town'),
    path('total_voters/', total_voters, name='total_voters'),
    path('get_all_voters/', get_all_voters, name = 'get_all_voters'),
    path('BoothCountView/', BoothCountView.as_view(), name = 'BoothCountView'),
    path('TownCountView/', TownCountView.as_view(), name = 'TownCountView'),
    path('religions/', ReligionListView.as_view(), name='religion-list'),
    path('religion/<int:religion_id>/', VoterlistByReligion.as_view(), name='voter-list-by-religion'),
    path('religion_wise_voter_list/<int:religion_id>/', VoterlistByReligionView.as_view(), name='voter-list-by-religion'),
    path('update_town/', update_town_panchayat, name='update-town-panchayat'),   #create panchayat samiti circle and assign panchayat samiti circle to town
    path('panchayat_samiti_circle/', get_panchayat_samiti_circle, name='panchayat_samiti_circle'),
    path('update_panchayat_circle/', update_panchayat_circle, name='update_panchayat_circle'),
    


    
# admin pannel 
    path('admin/', include('accounts.urls'))
    


]
