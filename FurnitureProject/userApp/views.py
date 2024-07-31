from django.shortcuts import redirect, render

from adminApp.models import AboutModel, Bgc1Model, Bgc2Model, Bgc3Model, Bgc4Model, BlogModel, BsliderModel, BsvideoModel, BtopicModel, BvideoModel, CfeedbackModel, Cgc1Model, Cgc2Model, Cgc3Model, Cgc4Model, ContactModel, CsliderModel, CsvideoModel, CtopicModel, CvideoModel, Hgc1Model, Hgc2Model, Hgc3Model, Hgc4Model, HsliderModel, HsvideoModel, HtopicModel, HvideoModel, Kgc1Model, Kgc2Model, Kgc3Model, Kgc4Model, KsliderModel, KsvideoModel, KtopicModel, KvideoModel, Lgc1Model, Lgc2Model, Lgc3Model, Lgc4Model, LsliderModel, LsvideoModel, LtopicModel, LvideoModel, MemberModel, Ofgc1Model, Ofgc2Model, Ofgc3Model, Ofgc4Model, OfsliderModel, OfsvideoModel, OftopicModel, OfvideoModel, Ogc1Model, Ogc2Model, Ogc3Model, Ogc4Model, OsliderModel, OsvideoModel, Otgc1Model, Otgc2Model, Otgc3Model, Otgc4Model, OtopicModel, OtsvideoModel, OttopicModel, OvideoModel
from userApp.models import CContactModel

 
# Create your views here.
def home(r):
    hsliderimgs = HsliderModel.objects.all()
    hvideos = HvideoModel.objects.filter(id=1)
    htopics = HtopicModel.objects.all()
    hsvideos = HsvideoModel.objects.all()
    hgc1imgs = Hgc1Model.objects.all()
    hgc2imgs = Hgc2Model.objects.all()
    hgc3imgs = Hgc3Model.objects.all()
    hgc4imgs = Hgc4Model.objects.all()
    feedbacks = CfeedbackModel.objects.all()

    obj = {
        "hsliderimgs":hsliderimgs,
        "hvideos":hvideos,
        "htopics":htopics,
        "hsvideos":hsvideos,
        "hgc1imgs":hgc1imgs,
        "hgc2imgs":hgc2imgs,
        "hgc3imgs":hgc3imgs,
        "hgc4imgs":hgc4imgs,
        "feedbacks":feedbacks
    }
    return render(r,"user/home.html",obj)

def living(r):
    lsliderimgs = LsliderModel.objects.all()
    lvideos = LvideoModel.objects.filter(id=1)
    ltopics = LtopicModel.objects.all()
    lsvideos = LsvideoModel.objects.all()
    lgc1imgs = Lgc1Model.objects.all()
    lgc2imgs = Lgc2Model.objects.all()
    lgc3imgs = Lgc3Model.objects.all()
    lgc4imgs = Lgc4Model.objects.all()
    

    obj = {
        "lsliderimgs":lsliderimgs,
        "lvideos":lvideos,
        "ltopics":ltopics,
        "lsvideos":lsvideos,
        "lgc1imgs":lgc1imgs,
        "lgc2imgs":lgc2imgs,
        "lgc3imgs":lgc3imgs,
        "lgc4imgs":lgc4imgs
        
    }
    return render(r,"user/living.html",obj)

def kitchen(r):
    ksliderimgs = KsliderModel.objects.all()
    kvideos = KvideoModel.objects.filter(id=1)
    ktopics = KtopicModel.objects.all()
    ksvideos = KsvideoModel.objects.all()
    kgc1imgs = Kgc1Model.objects.all()
    kgc2imgs = Kgc2Model.objects.all()
    kgc3imgs = Kgc3Model.objects.all()
    kgc4imgs = Kgc4Model.objects.all()
    

    obj = {
        "ksliderimgs":ksliderimgs,
        "kvideos":kvideos,
        "ktopics":ktopics,
        "ksvideos":ksvideos,
        "kgc1imgs":kgc1imgs,
        "kgc2imgs":kgc2imgs,
        "kgc3imgs":kgc3imgs,
        "kgc4imgs":kgc4imgs
        
    }
    return render(r,"user/kitchen.html",obj)

def bedroom(r):
    bsliderimgs = BsliderModel.objects.all()
    bvideos = BvideoModel.objects.filter(id=1)
    btopics = BtopicModel.objects.all()
    bsvideos = BsvideoModel.objects.all()
    bgc1imgs = Bgc1Model.objects.all()
    bgc2imgs = Bgc2Model.objects.all()
    bgc3imgs = Bgc3Model.objects.all()
    bgc4imgs = Bgc4Model.objects.all()
    

    obj = {
        "bsliderimgs":bsliderimgs,
        "bvideos":bvideos,
        "btopics":btopics,
        "bsvideos":bsvideos,
        "bgc1imgs":bgc1imgs,
        "bgc2imgs":bgc2imgs,
        "bgc3imgs":bgc3imgs,
        "bgc4imgs":bgc4imgs
        
    }
    return render(r,"user/bedroom.html",obj)

def outdoor(r):
    osliderimgs = OsliderModel.objects.all()
    ovideos = OvideoModel.objects.filter(id=1)
    otopics = OtopicModel.objects.all()
    osvideos = OsvideoModel.objects.all()
    ogc1imgs = Ogc1Model.objects.all()
    ogc2imgs = Ogc2Model.objects.all()
    ogc3imgs = Ogc3Model.objects.all()
    ogc4imgs = Ogc4Model.objects.all()
    

    obj = {
        "osliderimgs":osliderimgs,
        "ovideos":ovideos,
        "otopics":otopics,
        "osvideos":osvideos,
        "ogc1imgs":ogc1imgs,
        "ogc2imgs":ogc2imgs,
        "ogc3imgs":ogc3imgs,
        "ogc4imgs":ogc4imgs
        
    }
    return render(r,"user/outdoor.html",obj)

def cafe(r):
    csliderimgs = CsliderModel.objects.all()
    cvideos = CvideoModel.objects.filter(id=1)
    ctopics = CtopicModel.objects.all()
    csvideos = CsvideoModel.objects.all()
    cgc1imgs = Cgc1Model.objects.all()
    cgc2imgs = Cgc2Model.objects.all()
    cgc3imgs = Cgc3Model.objects.all()
    cgc4imgs = Cgc4Model.objects.all()
    

    obj = {
        "csliderimgs":csliderimgs,
        "cvideos":cvideos,
        "ctopics":ctopics,
        "csvideos":csvideos,
        "cgc1imgs":cgc1imgs,
        "cgc2imgs":cgc2imgs,
        "cgc3imgs":cgc3imgs,
        "cgc4imgs":cgc4imgs
        
    }
    return render(r,"user/cafe.html",obj)





def office(r):
    ofsliderimgs = OfsliderModel.objects.all()
    ofvideos = OfvideoModel.objects.filter(id=1)
    oftopics = OftopicModel.objects.all()
    ofsvideos = OfsvideoModel.objects.all()
    ofgc1imgs = Ofgc1Model.objects.all()
    ofgc2imgs = Ofgc2Model.objects.all()
    ofgc3imgs = Ofgc3Model.objects.all()
    ofgc4imgs = Ofgc4Model.objects.all()
    

    obj = {
        "ofsliderimgs":ofsliderimgs,
        "ofvideos":ofvideos,
        "oftopics":oftopics,
        "ofsvideos":ofsvideos,
        "ofgc1imgs":ofgc1imgs,
        "ofgc2imgs":ofgc2imgs,
        "ofgc3imgs":ofgc3imgs,
        "ofgc4imgs":ofgc4imgs
        
    }
    return render(r,"user/office.html",obj)




def others(r):
    
    ottopics = OttopicModel.objects.all()
    otsvideos = OtsvideoModel.objects.all()
    otgc1imgs = Otgc1Model.objects.all()
    otgc2imgs = Otgc2Model.objects.all()
    otgc3imgs = Otgc3Model.objects.all()
    otgc4imgs = Otgc4Model.objects.all()
    

    obj = {
        
        "ottopics":ottopics,
        "otsvideos":otsvideos,
        "otgc1imgs":otgc1imgs,
        "otgc2imgs":otgc2imgs,
        "otgc3imgs":otgc3imgs,
        "otgc4imgs":otgc4imgs
        
    }
    return render(r,"user/others.html",obj)




def about_us(r):
    about_us= AboutModel.objects.all()
    members = MemberModel.objects.all()

    
    return render(r,"user/about_us.html",{"about_us":about_us, "members":members})






def blogs(r):
    blogs = BlogModel.objects.all()

    return render(r,"user/blogs.html",{"blogs":blogs})




def contact_us(r):
    contacts = ContactModel.objects.get(id=1)

    ccontacts = CContactModel.objects.all()

    return render(r,"user/contact_us.html",{"ccontacts":ccontacts, "contacts":contacts})

def save_contact(r):
    newccontact = CContactModel(
        cname = r.POST['cname'],
        cmobile = r.POST['cmobile'],
        cemail = r.POST['cemail'],
        ccity = r.POST['ccity'],
        cmessage = r.POST['cmessage']
    )
    newccontact.save()

    return redirect("/contact_us") 