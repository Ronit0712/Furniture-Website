from django.urls import path
from adminApp import views

urlpatterns=[
    path('',views.login),
    path('do_login/',views.do_login),
  
    path('home/',views.home),

    path('save_hsliderimg/',views.save_hsliderimg),
    path('delete_hsliderimg/',views.delete_hsliderimg),

    path('save_hvideos/',views.save_hvideos),

    path('save_htopic/',views.save_htopic),
    path('delete_htopic/',views.delete_htopic),

    path('save_hsvideo/',views.save_hsvideo),
    path('delete_hsvideo/',views.delete_hsvideo),

    path('save_hgc1img/',views.save_hgc1img),
    path('delete_hgc1img/',views.delete_hgc1img),

    path('save_hgc2img/',views.save_hgc2img),
    path('delete_hgc2img/',views.delete_hgc2img),

    path('save_hgc3img/',views.save_hgc3img),
    path('delete_hgc3img/',views.delete_hgc3img),
    
    path('save_hgc4img/',views.save_hgc4img),
    path('delete_hgc4img/',views.delete_hgc4img),

    path('save_feedback/',views.save_feedback),
    path('delete_feedback/',views.delete_feedback),


# Living -----------------------------------------------------------------------------------

    path('living/',views.living),
    path('save_lsliderimg/',views.save_lsliderimg),
    path('delete_lsliderimg/',views.delete_lsliderimg),

    path('save_lvideos/',views.save_lvideos),
  
    path('save_ltopic/',views.save_ltopic),
    path('delete_ltopic/',views.delete_ltopic),

    path('save_lsvideo/',views.save_lsvideo),
    path('delete_lsvideo/',views.delete_lsvideo),

    path('save_lgc1img/',views.save_lgc1img),
    path('delete_lgc1img/',views.delete_lgc1img),

    path('save_lgc2img/',views.save_lgc2img),
    path('delete_lgc2img/',views.delete_lgc2img),

    path('save_lgc3img/',views.save_lgc3img),
    path('delete_lgc3img/',views.delete_lgc3img),
    
    path('save_lgc4img/',views.save_lgc4img),
    path('delete_lgc4img/',views.delete_lgc4img),


# Kitchen ------------------------------------------------------------------------------------

    path('kitchen/',views.kitchen),
    path('save_ksliderimg/',views.save_ksliderimg),
    path('delete_ksliderimg/',views.delete_ksliderimg),

    path('save_kvideos/',views.save_kvideos),
  
    path('save_ktopic/',views.save_ktopic),
    path('delete_ktopic/',views.delete_ktopic),

    path('save_ksvideo/',views.save_ksvideo),
    path('delete_ksvideo/',views.delete_ksvideo),

    path('save_kgc1img/',views.save_kgc1img),
    path('delete_kgc1img/',views.delete_kgc1img),

    path('save_kgc2img/',views.save_kgc2img),
    path('delete_kgc2img/',views.delete_kgc2img),

    path('save_kgc3img/',views.save_kgc3img),
    path('delete_kgc3img/',views.delete_kgc3img),
    
    path('save_kgc4img/',views.save_kgc4img),
    path('delete_kgc4img/',views.delete_kgc4img),



# Bedroom -------------------------------------------------------------------

    path('bedroom/',views.bedroom),
    path('save_bsliderimg/',views.save_bsliderimg),
    path('delete_bsliderimg/',views.delete_bsliderimg),

    path('save_bvideos/',views.save_bvideos),
  
    path('save_btopic/',views.save_btopic),
    path('delete_btopic/',views.delete_btopic),

    path('save_bsvideo/',views.save_bsvideo),
    path('delete_bsvideo/',views.delete_bsvideo),

    path('save_bgc1img/',views.save_bgc1img),
    path('delete_bgc1img/',views.delete_bgc1img),

    path('save_bgc2img/',views.save_bgc2img),
    path('delete_bgc2img/',views.delete_bgc2img),

    path('save_bgc3img/',views.save_bgc3img),
    path('delete_bgc3img/',views.delete_bgc3img),
    
    path('save_bgc4img/',views.save_bgc4img),
    path('delete_bgc4img/',views.delete_bgc4img),



# Outdoor --------------------------------------------------------------------------

    path('outdoor/',views.outdoor),
    path('save_osliderimg/',views.save_osliderimg),
    path('delete_osliderimg/',views.delete_osliderimg),

    path('save_ovideos/',views.save_ovideos),
  
    path('save_otopic/',views.save_otopic),
    path('delete_otopic/',views.delete_otopic),

    path('save_osvideo/',views.save_osvideo),
    path('delete_osvideo/',views.delete_osvideo),

    path('save_ogc1img/',views.save_ogc1img),
    path('delete_ogc1img/',views.delete_ogc1img),

    path('save_ogc2img/',views.save_ogc2img),
    path('delete_ogc2img/',views.delete_ogc2img),

    path('save_ogc3img/',views.save_ogc3img),
    path('delete_ogc3img/',views.delete_ogc3img),
    
    path('save_ogc4img/',views.save_ogc4img),
    path('delete_ogc4img/',views.delete_ogc4img),



# Cafe ---------------------------------------------------------------------------------

    path('cafe/',views.cafe),
    path('save_csliderimg/',views.save_csliderimg),
    path('delete_csliderimg/',views.delete_csliderimg),

    path('save_cvideos/',views.save_cvideos),
  
    path('save_ctopic/',views.save_ctopic),
    path('delete_ctopic/',views.delete_ctopic),

    path('save_csvideo/',views.save_csvideo),
    path('delete_csvideo/',views.delete_csvideo),

    path('save_cgc1img/',views.save_cgc1img),
    path('delete_cgc1img/',views.delete_cgc1img),

    path('save_cgc2img/',views.save_cgc2img),
    path('delete_cgc2img/',views.delete_cgc2img),

    path('save_cgc3img/',views.save_cgc3img),
    path('delete_cgc3img/',views.delete_cgc3img),
    
    path('save_cgc4img/',views.save_cgc4img),
    path('delete_cgc4img/',views.delete_cgc4img),



# office ----------------------------------------------------------------------------

    path('office/',views.office),
    path('save_ofsliderimg/',views.save_ofsliderimg),
    path('delete_ofsliderimg/',views.delete_ofsliderimg),

    path('save_ofvideos/',views.save_ofvideos),
  
    path('save_oftopic/',views.save_oftopic),
    path('delete_oftopic/',views.delete_oftopic),

    path('save_ofsvideo/',views.save_ofsvideo),
    path('delete_ofsvideo/',views.delete_ofsvideo),

    path('save_ofgc1img/',views.save_ofgc1img),
    path('delete_ofgc1img/',views.delete_ofgc1img),

    path('save_ofgc2img/',views.save_ofgc2img),
    path('delete_ofgc2img/',views.delete_ofgc2img),

    path('save_ofgc3img/',views.save_ofgc3img),
    path('delete_ofgc3img/',views.delete_ofgc3img),
    
    path('save_ofgc4img/',views.save_ofgc4img),
    path('delete_ofgc4img/',views.delete_ofgc4img),



# Others ---------------------------------------------------------------------------

    path('others/',views.others),
    path('save_ottopic/',views.save_ottopic),
    path('delete_ottopic/',views.delete_ottopic),

    path('save_otsvideo/',views.save_otsvideo),
    path('delete_otsvideo/',views.delete_otsvideo),

    path('save_otgc1img/',views.save_otgc1img),
    path('delete_otgc1img/',views.delete_otgc1img),

    path('save_otgc2img/',views.save_otgc2img),
    path('delete_otgc2img/',views.delete_otgc2img),

    path('save_otgc3img/',views.save_otgc3img),
    path('delete_otgc3img/',views.delete_otgc3img),
    
    path('save_otgc4img/',views.save_otgc4img),
    path('delete_otgc4img/',views.delete_otgc4img),



#About --------------------------------------------------------------------------

    path('about_us/',views.about_us),
    path('save_about/',views.save_about),
    path('delete_about/',views.delete_about),

    path('save_member/',views.save_member),
    path('delete_member/',views.delete_member),




#Blogs ------------------------------------------------------------------------

    path('blog/',views.blog),
    path('save_blog/',views.save_blog),
    path('delete_blog/',views.delete_blog),



#Contact_us ---------------------------------------------------------------------

    path('contact_us/',views.contact_us),
    path('save_contact/',views.save_contact),
    path('delete_contact/',views.delete_contact)





]