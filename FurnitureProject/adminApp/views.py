from django.shortcuts import redirect, render
from adminApp.models import AboutModel, AdminModel, Bgc1Model, Bgc2Model, Bgc3Model, Bgc4Model, BlogModel, BsliderModel, BsvideoModel, BtopicModel, BvideoModel, CfeedbackModel, Cgc1Model, Cgc2Model, Cgc3Model, Cgc4Model, ContactModel, CsliderModel, CsvideoModel, CtopicModel, CvideoModel, Hgc1Model, Hgc2Model, Hgc3Model, Hgc4Model, HsliderModel, HsvideoModel, HtopicModel, HvideoModel, Kgc1Model, Kgc2Model, Kgc3Model, Kgc4Model, KsliderModel, KsvideoModel, KtopicModel, KvideoModel, Lgc1Model, Lgc2Model, Lgc3Model, Lgc4Model, LsliderModel, LsvideoModel, LtopicModel, LvideoModel, MemberModel, Ofgc1Model, Ofgc2Model, Ofgc3Model, Ofgc4Model, OfsliderModel, OfsvideoModel, OftopicModel, OfvideoModel, Ogc1Model, Ogc2Model, Ogc3Model, Ogc4Model, OsliderModel, OsvideoModel, Otgc1Model, Otgc2Model, Otgc3Model, Otgc4Model, OtopicModel, OtsvideoModel, OttopicModel, OvideoModel
from userApp.models import CContactModel
# Create your views here.
def login(r):
    return render(r,"admin/login.html")

def do_login(r):
    # newuser = AdminModel()
    # newuser.username = r.POST['username'],
    # newuser.password = r.POST['password']
    # newuser.save()
    # return redirect("/admin/home")

    # print(r.POST)

    check_admin = AdminModel.objects.filter(
        username= r.POST['username'],
        password = r.POST['password']
    )
    if(len(check_admin)>0):
        r.session['user_id']=check_admin[0].id
        return redirect("/admin/home")
    else:
        return redirect("/admin")





# Home --------------------------------------------------------------------------------
def home(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    
    hsliderimgs = HsliderModel.objects.all()
    hvideos = HvideoModel.objects.get(id=1)
    htopics = HtopicModel.objects.all()
    hsvideos = HsvideoModel.objects.all()
    hgc1imgs = Hgc1Model.objects.all()
    hgc2imgs = Hgc2Model.objects.all()
    hgc3imgs = Hgc3Model.objects.all()
    hgc4imgs = Hgc4Model.objects.all()
    feedbacks = CfeedbackModel.objects.all()

    return render(r,"admin/home.html", {"hsliderimgs":hsliderimgs, "hvideos":hvideos, "htopics":htopics, "hsvideos":hsvideos, "hgc1imgs":hgc1imgs, "hgc2imgs":hgc2imgs, "hgc3imgs":hgc3imgs, "hgc4imgs":hgc4imgs, "feedbacks":feedbacks})

# ----------------------------------------------------------------

def save_hsliderimg(r):
    newhsliderimg = HsliderModel(
        hsliderimg = r.FILES['hsliderimg']
    )
    newhsliderimg.save()
    return redirect("/admin/home")

def delete_hsliderimg(r):
    HsliderModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/home")

# -----------------------------------------------------------------

def save_hvideos(r):
    # newhvideos = HvideoModel(
    #     hvideo1 = r.FILES['hvideo1'],
    #     hvideo2 = r.FILES['hvideo2']
    # )
    # newhvideos.save()

    update_hvideo = HvideoModel.objects.get(id=1)
    
    if"hvideo1" in r.FILES:
        update_hvideo.hvideo1 = r.FILES['hvideo1']

    if"hvideo2" in r.FILES:
        update_hvideo.hvideo2 = r.FILES['hvideo2']
    
    return redirect("/admin/home")

# ------------------------------------------------------------------

def save_htopic(r):
    newhtopic = HtopicModel(
        htopicimg = r.FILES['htopicimg'],
        htopicimgt = r.POST['htopicimgt']
    ) 
    newhtopic.save()

    return redirect("/admin/home")

def delete_htopic(r):
    HtopicModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/home")

# ---------------------------------------------------------------------------------------

def save_hsvideo(r):
    newhsvideo = HsvideoModel(
        hsvideo = r.FILES['hsvideo']
    )
    newhsvideo.save()
    return redirect("/admin/home")

def delete_hsvideo(r):
    HsvideoModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/home")

# ----------------------------------------------------------------------------------------

def save_hgc1img(r):
    newhgc1img = Hgc1Model(
        hgc1img = r.FILES['hgc1img']
    )
    newhgc1img.save()
    return redirect("/admin/home")

def delete_hgc1img(r):
    Hgc1Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/home")
    


def save_hgc2img(r):
    newhgc2img = Hgc2Model(
        hgc2img = r.FILES['hgc2img']
    )
    newhgc2img.save()
    return redirect("/admin/home")

def delete_hgc2img(r):
    Hgc2Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/home")


def save_hgc3img(r):
    newhgc3img = Hgc3Model(
        hgc3img = r.FILES['hgc3img']
    )
    newhgc3img.save()
    return redirect("/admin/home")

def delete_hgc3img(r):
    Hgc3Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/home")


def save_hgc4img(r):
    newhgc4img = Hgc4Model(
        hgc4img = r.FILES['hgc4img']
    )
    newhgc4img.save()
    return redirect("/admin/home")

def delete_hgc4img(r):
    Hgc4Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/home")

# -------------------------------------------------------------------------------------

def save_feedback(r):
    newfeedback = CfeedbackModel(
        fimg = r.FILES['fimg'],
        cpimg = r.FILES['cpimg'],
        cname = r.POST['cname'],
        cfeedback = r.POST['cfeedback']
    )
    newfeedback.save()
    return redirect("/admin/home")

def delete_feedback(r):
    CfeedbackModel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/home")







#LIVING ----------------------------------------------------------------------------------------

def living(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    
    lsliderimgs = LsliderModel.objects.all()
    lvideos = LvideoModel.objects.get(id=1)
    ltopics = LtopicModel.objects.all()
    lsvideos = LsvideoModel.objects.all()
    lgc1imgs = Lgc1Model.objects.all()
    lgc2imgs = Lgc2Model.objects.all()
    lgc3imgs = Lgc3Model.objects.all()
    lgc4imgs = Lgc4Model.objects.all()


    return render(r,"admin/living.html", {"lsliderimgs":lsliderimgs, "lvideos":lvideos, "ltopics":ltopics, "lsvideos":lsvideos, "lgc1imgs":lgc1imgs, "lgc2imgs":lgc2imgs, "lgc3imgs":lgc3imgs, "lgc4imgs":lgc4imgs})

def save_lsliderimg(r):
    newlsliderimg = LsliderModel(
        lsliderimg = r.FILES['lsliderimg']
    )
    newlsliderimg.save()
    return redirect("/admin/living")

def delete_lsliderimg(r):
    LsliderModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/living")

# ---------------------------------------------------------------------------------------

def save_lvideos(r):
    # newlvideos = LvideoModel(
    #     lvideo1 = r.FILES['lvideo1'],
    #     lvideo2 = r.FILES['lvideo2']
    # )
    # newlvideos.save()

    update_lvideo = LvideoModel.objects.get(id=1)
    
    if"lvideo1" in r.FILES:
        update_lvideo.lvideo1 = r.FILES['lvideo1']

    if"lvideo2" in r.FILES:
        update_lvideo.lvideo2 = r.FILES['lvideo2']
    
    return redirect("/admin/living")

# --------------------------------------------------------------------------------------

def save_ltopic(r):
    newltopic = LtopicModel(
        ltopicimg = r.FILES['ltopicimg'],
        ltopicimgt = r.POST['ltopicimgt']
    ) 
    newltopic.save()

    return redirect("/admin/living")

def delete_ltopic(r):
    LtopicModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/living")

# ----------------------------------------------------------------------------------------
def save_lsvideo(r):
    newlsvideo = LsvideoModel(
        lsvideo = r.FILES['lsvideo']
    )
    newlsvideo.save()
    return redirect("/admin/living")

def delete_lsvideo(r):
    LsvideoModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/living")

# ----------------------------------------------------------------------------------------
def save_lgc1img(r):
    newlgc1img = Lgc1Model(
        lgc1img = r.FILES['lgc1img']
    )
    newlgc1img.save()
    return redirect("/admin/living")

def delete_lgc1img(r):
    Lgc1Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/living")
    


def save_lgc2img(r):
    newlgc2img = Lgc2Model(
        lgc2img = r.FILES['lgc2img']
    )
    newlgc2img.save()
    return redirect("/admin/living")

def delete_lgc2img(r):
    Lgc2Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/living")


def save_lgc3img(r):
    newlgc3img = Lgc3Model(
        lgc3img = r.FILES['lgc3img']
    )
    newlgc3img.save()
    return redirect("/admin/living")

def delete_lgc3img(r):
    Lgc3Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/living")


def save_lgc4img(r):
    newlgc4img = Lgc4Model(
        lgc4img = r.FILES['lgc4img']
    )
    newlgc4img.save()
    return redirect("/admin/living")

def delete_lgc4img(r):
    Lgc4Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/living")






#Kitchen ----------------------------------------------------------------------------------------

def kitchen(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    ksliderimgs = KsliderModel.objects.all()
    kvideos = KvideoModel.objects.all()
    ktopics = KtopicModel.objects.all()
    ksvideos = KsvideoModel.objects.all()
    kgc1imgs = Kgc1Model.objects.all()
    kgc2imgs = Kgc2Model.objects.all()
    kgc3imgs = Kgc3Model.objects.all()
    kgc4imgs = Kgc4Model.objects.all()

    return render(r,"admin/kitchen.html",{"ksliderimgs":ksliderimgs,"kvideos":kvideos,"ktopics":ktopics,"ksvideos":ksvideos,"kgc1imgs":kgc1imgs,"kgc2imgs":kgc2imgs,"kgc3imgs":kgc3imgs,"kgc4imgs":kgc4imgs,})

def save_ksliderimg(r):
    newksliderimg = KsliderModel(
        ksliderimg = r.FILES['ksliderimg']
    )
    newksliderimg.save()
    return redirect("/admin/kitchen")

def delete_ksliderimg(r):
    KsliderModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/kitchen")

# ---------------------------------------------------------------------------------------

def save_kvideos(r):
    newkvideos = KvideoModel(
        kvideo1 = r.FILES['kvideo1'],
        kvideo2 = r.FILES['kvideo2']
    )
    newkvideos.save()

    # update_kvideo = KvideoModel.objects.get(id=1)
    
    # if"kvideo1" in r.FILES:
    #     update_kvideo.kvideo1 = r.FILES['kvideo1']

    # if"kvideo2" in r.FILES:
    #     update_kvideo.kvideo2 = r.FILES['kvideo2']
    
    return redirect("/admin/kitchen")

# --------------------------------------------------------------------------------------

def save_ktopic(r):
    newktopic = KtopicModel(
        ktopicimg = r.FILES['ktopicimg'],
        ktopicimgt = r.POST['ktopicimgt']
    ) 
    newktopic.save()

    return redirect("/admin/kitchen")

def delete_ktopic(r):
    KtopicModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/kitchen")

# ----------------------------------------------------------------------------------------
def save_ksvideo(r):
    newksvideo = KsvideoModel(
        ksvideo = r.FILES['ksvideo']
    )
    newksvideo.save()
    return redirect("/admin/kitchen")

def delete_ksvideo(r):
    KsvideoModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/kitchen")

# ----------------------------------------------------------------------------------------
def save_kgc1img(r):
    newkgc1img = Kgc1Model(
        kgc1img = r.FILES['kgc1img']
    )
    newkgc1img.save()
    return redirect("/admin/kitchen")

def delete_kgc1img(r):
    Kgc1Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/kitchen")
    


def save_kgc2img(r):
    newkgc2img = Kgc2Model(
        kgc2img = r.FILES['kgc2img']
    )
    newkgc2img.save()
    return redirect("/admin/kitchen")

def delete_kgc2img(r):
    Kgc2Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/kitchen")


def save_kgc3img(r):
    newkgc3img = Kgc3Model(
        kgc3img = r.FILES['kgc3img']
    )
    newkgc3img.save()
    return redirect("/admin/kitchen")

def delete_kgc3img(r):
    Kgc3Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/kitchen")


def save_kgc4img(r):
    newkgc4img = Kgc4Model(
        kgc4img = r.FILES['kgc4img']
    )
    newkgc4img.save()
    return redirect("/admin/kitchen")

def delete_kgc4img(r):
    Kgc4Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/kitchen")






#Bedroom--------------------------------------------------------------------------------

def bedroom(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    
    bsliderimgs = BsliderModel.objects.all()
    bvideos = BvideoModel.objects.all()
    btopics = BtopicModel.objects.all()
    bsvideos = BsvideoModel.objects.all()
    bgc1imgs = Bgc1Model.objects.all()
    bgc2imgs = Bgc2Model.objects.all()
    bgc3imgs = Bgc3Model.objects.all()
    bgc4imgs = Bgc4Model.objects.all()
    return render(r,"admin/bedroom.html",{"bsliderimgs":bsliderimgs, "bvideos":bvideos,"btopics":btopics,"bsvideos":bsvideos,"bgc1imgs":bgc1imgs,"bgc2imgs":bgc2imgs,"bgc3imgs":bgc3imgs,"bgc4imgs":bgc4imgs,})

def save_bsliderimg(r):
    newbsliderimg = BsliderModel(
        bsliderimg = r.FILES['bsliderimg']
    )
    newbsliderimg.save()
    return redirect("/admin/bedroom")

def delete_bsliderimg(r):
    BsliderModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/bedroom")

# ---------------------------------------------------------------------------------------

def save_bvideos(r):
    newbvideos = BvideoModel(
        bvideo1 = r.FILES['bvideo1'],
        bvideo2 = r.FILES['bvideo2']
    )
    newbvideos.save()

    # update_bvideo = BvideoModel.objects.get(id=1)
    
    # if"bvideo1" in r.FILES:
    #     update_bvideo.bvideo1 = r.FILES['bvideo1']

    # if"bvideo2" in r.FILES:
    #     update_bvideo.bvideo2 = r.FILES['bvideo2']
    
    return redirect("/admin/bedroom")

# --------------------------------------------------------------------------------------

def save_btopic(r):
    newbtopic = BtopicModel(
        btopicimg = r.FILES['btopicimg'],
        btopicimgt = r.POST['btopicimgt']
    ) 
    newbtopic.save()

    return redirect("/admin/bedroom")

def delete_btopic(r):
    BtopicModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/bedroom")

# ----------------------------------------------------------------------------------------
def save_bsvideo(r):
    newbsvideo = BsvideoModel(
        bsvideo = r.FILES['bsvideo']
    )
    newbsvideo.save()
    return redirect("/admin/bedroom")

def delete_bsvideo(r):
    BsvideoModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/bedroom")

# ----------------------------------------------------------------------------------------
def save_bgc1img(r):
    newbgc1img = Bgc1Model(
        bgc1img = r.FILES['bgc1img']
    )
    newbgc1img.save()
    return redirect("/admin/bedroom")

def delete_bgc1img(r):
    Bgc1Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/bedroom")
    


def save_bgc2img(r):
    newbgc2img = Bgc2Model(
        bgc2img = r.FILES['bgc2img']
    )
    newbgc2img.save()
    return redirect("/admin/bedroom")

def delete_bgc2img(r):
    Bgc2Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/bedroom")


def save_bgc3img(r):
    newbgc3img = Bgc3Model(
        bgc3img = r.FILES['bgc3img']
    )
    newbgc3img.save()
    return redirect("/admin/bedroom")

def delete_bgc3img(r):
    Bgc3Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/bedroom")


def save_bgc4img(r):
    newbgc4img = Bgc4Model(
        bgc4img = r.FILES['bgc4img']
    )
    newbgc4img.save()
    return redirect("/admin/bedroom")

def delete_bgc4img(r):
    Bgc4Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/bedroom")







# Outdoor -------------------------------------------------------------------------------

def outdoor(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    
    osliderimgs = OsliderModel.objects.all()
    ovideos = OvideoModel.objects.all()
    otopics = OtopicModel.objects.all()
    osvideos = OsvideoModel.objects.all()
    ogc1imgs = Ogc1Model.objects.all()
    ogc2imgs = Ogc2Model.objects.all()
    ogc3imgs = Ogc3Model.objects.all()
    ogc4imgs = Ogc4Model.objects.all()
    return render(r,"admin/outdoor.html",{"osliderimgs":osliderimgs,"ovideos":ovideos,"otopics":otopics,"osvideos":osvideos,"ogc1imgs":ogc1imgs,"ogc2imgs":ogc2imgs,"ogc3imgs":ogc3imgs,"ogc4imgs":ogc4imgs,})

def save_osliderimg(r):
    newosliderimg = OsliderModel(
        osliderimg = r.FILES['osliderimg']
    )
    newosliderimg.save()
    return redirect("/admin/outdoor")

def delete_osliderimg(r):
    OsliderModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/outdoor")

# ---------------------------------------------------------------------------------------

def save_ovideos(r):
    newovideos = OvideoModel(
        ovideo1 = r.FILES['ovideo1'],
        ovideo2 = r.FILES['ovideo2']
    )
    newovideos.save()

    # update_ovideo = OvideoModel.objects.get(id=1)
    
    # if"ovideo1" in r.FILES:
    #     update_ovideo.ovideo1 = r.FILES['ovideo1']

    # if"ovideo2" in r.FILES:
    #     update_ovideo.ovideo2 = r.FILES['ovideo2']
    
    return redirect("/admin/outdoor")

# --------------------------------------------------------------------------------------

def save_otopic(r):
    newotopic = OtopicModel(
        otopicimg = r.FILES['otopicimg'],
        otopicimgt = r.POST['otopicimgt']
    ) 
    newotopic.save()

    return redirect("/admin/outdoor")

def delete_otopic(r):
    OtopicModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/outdoor")

# ----------------------------------------------------------------------------------------
def save_osvideo(r):
    newosvideo = OsvideoModel(
        osvideo = r.FILES['osvideo']
    )
    newosvideo.save()
    return redirect("/admin/outdoor")

def delete_osvideo(r):
    OsvideoModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/outdoor")

# ----------------------------------------------------------------------------------------
def save_ogc1img(r):
    newogc1img = Ogc1Model(
        ogc1img = r.FILES['ogc1img']
    )
    newogc1img.save()
    return redirect("/admin/outdoor")

def delete_ogc1img(r):
    Ogc1Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/outdoor")
    


def save_ogc2img(r):
    newogc2img = Ogc2Model(
        ogc2img = r.FILES['ogc2img']
    )
    newogc2img.save()
    return redirect("/admin/outdoor")

def delete_ogc2img(r):
    Ogc2Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/outdoor")


def save_ogc3img(r):
    newogc3img = Ogc3Model(
        ogc3img = r.FILES['ogc3img']
    )
    newogc3img.save()
    return redirect("/admin/outdoor")

def delete_ogc3img(r):
    Ogc3Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/outdoor")


def save_ogc4img(r):
    newogc4img = Ogc4Model(
        ogc4img = r.FILES['ogc4img']
    )
    newogc4img.save()
    return redirect("/admin/outdoor")

def delete_ogc4img(r):
    Ogc4Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/outdoor")








# Cafe ----------------------------------------------------------------------------------

def cafe(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
     
    csliderimgs = CsliderModel.objects.all()
    cvideos = CvideoModel.objects.all()
    ctopics = CtopicModel.objects.all()
    csvideos = CsvideoModel.objects.all()
    cgc1imgs = Cgc1Model.objects.all()
    cgc2imgs = Cgc2Model.objects.all()
    cgc3imgs = Cgc3Model.objects.all()
    cgc4imgs = Cgc4Model.objects.all()
    return render(r,"admin/cafe.html",{"csliderimgs":csliderimgs,"cvideos":cvideos,"ctopics":ctopics,"csvideos":csvideos,"cgc1imgs":cgc1imgs,"cgc2imgs":cgc2imgs,"cgc3imgs":cgc3imgs,"cgc4imgs":cgc4imgs})


def save_csliderimg(r):
    newcsliderimg = CsliderModel(
        csliderimg = r.FILES['csliderimg']
    )
    newcsliderimg.save()
    return redirect("/admin/cafe")

def delete_csliderimg(r):
    CsliderModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/cafe")

# ---------------------------------------------------------------------------------------

def save_cvideos(r):
    newcvideos = CvideoModel(
        cvideo1 = r.FILES['cvideo1'],
        cvideo2 = r.FILES['cvideo2']
    )
    newcvideos.save()

    # update_cvideo = CvideoModel.objects.get(id=1)
    
    # if"cvideo1" in r.FILES:
    #     update_cvideo.cvideo1 = r.FILES['cvideo1']

    # if"cvideo2" in r.FILES:
    #     update_cvideo.cvideo2 = r.FILES['cvideo2']
    
    return redirect("/admin/cafe")

# --------------------------------------------------------------------------------------

def save_ctopic(r):
    newctopic = CtopicModel(
        ctopicimg = r.FILES['ctopicimg'],
        ctopicimgt = r.POST['ctopicimgt']
    ) 
    newctopic.save()

    return redirect("/admin/cafe")

def delete_ctopic(r):
    CtopicModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/cafe")

# ----------------------------------------------------------------------------------------
def save_csvideo(r):
    newcsvideo = CsvideoModel(
        csvideo = r.FILES['csvideo']
    )
    newcsvideo.save()
    return redirect("/admin/cafe")

def delete_csvideo(r):
    CsvideoModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/cafe")

# ----------------------------------------------------------------------------------------
def save_cgc1img(r):
    newcgc1img = Cgc1Model(
        cgc1img = r.FILES['cgc1img']
    )
    newcgc1img.save()
    return redirect("/admin/cafe")

def delete_cgc1img(r):
    Cgc1Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/cafe")
    


def save_cgc2img(r):
    newcgc2img = Cgc2Model(
        cgc2img = r.FILES['cgc2img']
    )
    newcgc2img.save()
    return redirect("/admin/cafe")

def delete_cgc2img(r):
    Cgc2Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/cafe")


def save_cgc3img(r):
    newcgc3img = Cgc3Model(
        cgc3img = r.FILES['cgc3img']
    )
    newcgc3img.save()
    return redirect("/admin/cafe")

def delete_cgc3img(r):
    Cgc3Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/cafe")


def save_cgc4img(r):
    newcgc4img = Cgc4Model(
        cgc4img = r.FILES['cgc4img']
    )
    newcgc4img.save()
    return redirect("/admin/cafe")

def delete_cgc4img(r):
    Cgc4Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/cafe")








# Office --------------------------------------------------------------------------------

def office(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
     
    ofsliderimgs = OfsliderModel.objects.all()
    ofvideos = OfvideoModel.objects.all()
    oftopics = OftopicModel.objects.all()
    ofsvideos = OfsvideoModel.objects.all()
    ofgc1imgs = Ofgc1Model.objects.all()
    ofgc2imgs = Ofgc2Model.objects.all()
    ofgc3imgs = Ofgc3Model.objects.all()
    ofgc4imgs = Ofgc4Model.objects.all()
    return render(r,"admin/office.html",{"ofsliderimgs":ofsliderimgs,"ofvideos":ofvideos,"oftopics":oftopics, "ofsvideos":ofsvideos, "ofgc1imgs":ofgc1imgs,"ofgc2imgs":ofgc2imgs,"ofgc3imgs":ofgc3imgs,"ofgc4imgs":ofgc4imgs,})



def save_ofsliderimg(r):
    newofsliderimg = OfsliderModel(
        ofsliderimg = r.FILES['ofsliderimg']
    )
    newofsliderimg.save()
    return redirect("/admin/office")

def delete_ofsliderimg(r):
    OfsliderModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/office")

# ---------------------------------------------------------------------------------------

def save_ofvideos(r):
    newofvideos = OfvideoModel(
        ofvideo1 = r.FILES['ofvideo1'],
        ofvideo2 = r.FILES['ofvideo2']
    )
    newofvideos.save()

    # update_ofvideo = OfvideoModel.objects.get(id=1)
    
    # if"ofvideo1" in r.FILES:
    #     update_ofvideo.ofvideo1 = r.FILES['ofvideo1']

    # if"ofvideo2" in r.FILES:
    #     update_ofvideo.ofvideo2 = r.FILES['ofvideo2']
    
    return redirect("/admin/office")

# --------------------------------------------------------------------------------------

def save_oftopic(r):
    newoftopic = OftopicModel(
        oftopicimg = r.FILES['oftopicimg'],
        oftopicimgt = r.POST['oftopicimgt']
    ) 
    newoftopic.save()

    return redirect("/admin/office")

def delete_oftopic(r):
    OftopicModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/office")

# ----------------------------------------------------------------------------------------
def save_ofsvideo(r):
    newofsvideo = OfsvideoModel(
        ofsvideo = r.FILES['ofsvideo']
    )
    newofsvideo.save()
    return redirect("/admin/office")

def delete_ofsvideo(r):
    OfsvideoModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/office")

# ----------------------------------------------------------------------------------------
def save_ofgc1img(r):
    newofgc1img = Ofgc1Model(
        ofgc1img = r.FILES['ofgc1img']
    )
    newofgc1img.save()
    return redirect("/admin/office")

def delete_ofgc1img(r):
    Ofgc1Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/office")
    
# ----------------------------------------------------------------------------------

def save_ofgc2img(r):
    newofgc2img = Ofgc2Model(
        ofgc2img = r.FILES['ofgc2img']
    )
    newofgc2img.save()
    return redirect("/admin/office")

def delete_ofgc2img(r):
    Ofgc2Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/office")

# ---------------------------------------------------------------------------------

def save_ofgc3img(r):
    newofgc3img = Ofgc3Model(
        ofgc3img = r.FILES['ofgc3img']
    )
    newofgc3img.save()
    return redirect("/admin/office")

def delete_ofgc3img(r):
    Ofgc3Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/office")

# -------------------------------------------------------------------------------

def save_ofgc4img(r):
    newofgc4img = Ofgc4Model(
        ofgc4img = r.FILES['ofgc4img']
    )
    newofgc4img.save()
    return redirect("/admin/office")

def delete_ofgc4img(r):
    Ofgc4Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/office")







# Others -------------------------------------------------------------------------------

def others(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    
    ottopics = OttopicModel.objects.all()
    otsvideos = OtsvideoModel.objects.all()
    otgc1imgs = Otgc1Model.objects.all()
    otgc2imgs = Otgc2Model.objects.all()
    otgc3imgs = Otgc3Model.objects.all()
    otgc4imgs = Otgc4Model.objects.all()
    return render(r,"admin/others.html", {"ottopics":ottopics, "otsvideos":otsvideos, "otgc1imgs":otgc1imgs, "otgc2imgs":otgc2imgs,"otgc3imgs":otgc3imgs,"otgc4imgs":otgc4imgs,})

def save_ottopic(r):
    newottopic = OttopicModel(
        ottopicimg = r.FILES['ottopicimg'],
        ottopicimgt = r.POST['ottopicimgt']
    ) 
    newottopic.save()

    return redirect("/admin/other")

def delete_ottopic(r):
    OttopicModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/other")

# ----------------------------------------------------------------------------------------
def save_otsvideo(r):
    newotsvideo = OtsvideoModel(
        otsvideo = r.FILES['otsvideo']
    )
    newotsvideo.save()
    return redirect("/admin/other")

def delete_otsvideo(r):
    OtsvideoModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/other")

# ----------------------------------------------------------------------------------------
def save_otgc1img(r):
    newotgc1img = Otgc1Model(
        otgc1img = r.FILES['otgc1img']
    )
    newotgc1img.save()
    return redirect("/admin/other")

def delete_otgc1img(r):
    Otgc1Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/other")
    

# ---------------------------------------------------------------------------------

def save_otgc2img(r):
    newotgc2img = Otgc2Model(
        otgc2img = r.FILES['otgc2img']
    )
    newotgc2img.save()
    return redirect("/admin/other")

def delete_otgc2img(r):
    Otgc2Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/other")

# -----------------------------------------------------------------------------------

def save_otgc3img(r):
    newotgc3img = Otgc3Model(
        otgc3img = r.FILES['otgc3img']
    )
    newotgc3img.save()
    return redirect("/admin/other")

def delete_otgc3img(r):
    Otgc3Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/other")

# ------------------------------------------------------------------------------------

def save_otgc4img(r):
    newotgc4img = Otgc4Model(
        otgc4img = r.FILES['otgc4img']
    )
    newotgc4img.save()
    return redirect("/admin/other")

def delete_otgc4img(r):
    Otgc4Model.objects.get(id= r.GET['id']).delete()
    return redirect("/admin/other")






#About ---------------------------------------------------------------------------------------

def about_us(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    
    about_us= AboutModel.objects.all()
    members = MemberModel.objects.all()
    return render(r,"admin/about_us.html",{"about_us":about_us, "members":members})

def save_about(r):
    newabout = AboutModel(
        abtitle = r.POST['abtitle'],
        abdis = r.POST['abdis']
    )
    newabout.save()

    return redirect("/admin/about_us")

def delete_about(r):
    AboutModel.objects.get(id=r.GET['id']).delete()

# --------------------------------------------------------------------------------
    
def save_member(r):
    newmember = MemberModel(
        tmphoto = r.FILES['tmphoto'],
        tmname = r.POST['tmname'],
        tmposition = r.POST['tmposition'],
        tmabout = r.POST['tmabout'],
        tmphone = r.POST['tmphone'],
    )
    newmember.save()

    return redirect("/admin/about_us")

def delete_member(r):
    MemberModel.objects.get(id=r.GET['id']).delete()
    return redirect("/admin/about_us")



#Blogs ---------------------------------------------------------------------------------
    

def blog(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    
    blogs = BlogModel.objects.all()
    return render(r,"admin/blog.html",{"blogs":blogs})

def save_blog(r):
    newblogs = BlogModel(
        bimage = r.FILES['bimage'],
        btitle = r.POST['btitle'],
        bdate = r.POST['bdate'],
        bdis = r.POST['bdis'],
        blog_by = r.POST['blog_by']
    )
    newblogs.save()

    return redirect("/admin/blog")

def delete_blog(r):
    BlogModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/blog")

 



#Contact --------------------------------------------------------------------------

def contact_us(r):
    if(not r.session.has_key('user_id')):
        return redirect("/admin")
    
    contacts = ContactModel.objects.get(id=1)
    ccontacts = CContactModel.objects.all()
    return render(r,"admin/contact_us.html", {"contacts":contacts, "ccontacts":ccontacts})

def save_contact(r):
    # newcontact = ContactModel(
    #     address = r.POST['address'],
    #     phoneno = r.POST['phoneno'],
    #     email = r.POST['email']
    # )
    # newcontact.save()

    update_contact = ContactModel.objects.get(id=1)
    update_contact.address = r.POST['address']
    update_contact.phoneno = r.POST['phoneno']
    update_contact.email = r.POST['email']

    update_contact.save()
    return redirect("/admin/contact_us")


def delete_contact(r):
    CContactModel.objects.get(id = r.GET['id']).delete()
    return redirect("/admin/contact_us")

