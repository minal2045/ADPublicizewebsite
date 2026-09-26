from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from pip._internal import req

from ADPublicize.forms import AdvertiserForm, PubliserForm, ContactusForm, AddlocationForm, AdvRequestForm
from ADPublicize.models import advertiser, publiser, contactus, SavLoc, advRequest
from django.contrib import messages
from django.core.files.storage import default_storage
from django.contrib.auth import authenticate, login


# home page
def home(request):
    return render(request, 'index.html')


# Adverrtiser Home Page
def advpage(request):
    return render(request, 'Advertiser/advertiserhome.html')


# Publisher Home
def pubpage(request):
    return render(request, 'Publisher/publisherhome.html')


# Regitration of Advertiser
def advreg(request):
    if request.method == "POST":
        form = AdvertiserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.INFO, 'Successfully Registered As A Advertiser')
                return redirect('/home')
            except:
                pass
    else:
        form = AdvertiserForm()
    return render(request, 'index.html', {'form': form})


# Publisher Registration
def pubreg(request):
    if request.method == "POST":
        form = PubliserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.INFO, 'Successfully Registered As A Publisher')
                return redirect('/home')
            except:
                pass
    else:
        form = PubliserForm()
    return render(request, 'index.html', {'form': form})


# Login
def clientlogin(request):
    if request.method == "POST":
        emailid = request.POST["emailid"]
        psw = request.POST["password"]
        rl = request.POST["role"]
        if rl == "advertiser":
            obj = advertiser.objects.get(emailid=request.POST["emailid"])
            if obj.password == request.POST["password"]:
                print("Email ID = ", emailid)
                request.session["loginid"] = obj.adverid
                request.session["fname"] = obj.fname
                # print("mail = ", emailid)
                # print("password = ", psw)
                return render(request, 'Advertiser/advertiserhome.html')
            else:
                messages.add_message(request, messages.ERROR, 'Username or Password or Role Invalid')
                return render(request, "index.html")
        elif rl == "publisher":
            obj1 = publiser.objects.get(emailid=request.POST["emailid"])
            if obj1.password == request.POST["password"]:
                print("Email ID = ", emailid)
                request.session["publogid"] = obj1.pubid
                request.session["fname"] = obj1.fname
                request.session["cname"] = obj1.cname
                # print("mail = ", emailid)
                # print("password = ", psw)
                return render(request, 'Publisher/publisherhome.html')
            else:
                messages.add_message(request, messages.ERROR, 'Username or Password or Role Invalid')
                return render(request, "index.html")
        else:
            messages.add_message(request, messages.ERROR, 'Role Invalid')
            return render(request, "index.html")
    return render(request, "index.html")


# logout
def logout(request):
    try:
        del request.session['loginid']
        del request.session['fname']
        del request.session['cname']
    except:
        return redirect(home)
    return redirect(home)


# Conatact Form
def contform(request):
    if request.method == "POST":
        form = ContactusForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.INFO, 'Successfully Sent a feedback')
                return redirect('/home')
            except:
                pass
    else:
        form = ContactusForm()
    return render(request, 'index.html', {'form': form})


# Add Advertisement Page in Publisher site
def adadvpage(request):
    return render(request, "Publisher/advertise.html")


# Form for add location
def addlocation(request):
    if request.method == "POST":
        form = AddlocationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Successfully Add location')
            return render(request, "Publisher/publisherhome.html")
    else:
        form = AddlocationForm()

    return render(request, 'Publisher/publisherhome.html', {'form': form})


# View location in Publisher site
def viewloc(request):
    lid = request.session.get("publogid")
    disppub = SavLoc.objects.filter(pubid=lid)
    return render(request, 'Publisher/pubviewloaction.html', {"disppub": disppub})


# View location in Advertise site
def advviewloc(request):
    disadv = SavLoc.objects.all()
    return render(request, 'Advertiser/advviewlocation.html', {"disadv": disadv})


# Show details of company at booking page in Advertise site
def pubdetails(request):
    if request.method == "POST":
        locid = request.POST["locid"]
        advtype = request.POST["advtype"]
        pubdtl = SavLoc.objects.get(locid=locid)
        if pubdtl:
            pub = {
                'data': pubdtl,
            }
        return render(request, 'Advertiser/filldeatils.html', pub)


# Advertiser Profile
def advertiserprofile(request):
    adverid = request.session.get("loginid")
    checkusr = advertiser.objects.filter(adverid=adverid)
    if checkusr:
        obj = advertiser.objects.get(adverid=adverid)
        usr = {
            'data': obj,
        }
        return render(request, 'Advertiser/advertiserprofile.html', usr)


# Publisher Profile
def publisherprofile(request):
    pubid = request.session.get("publogid")
    checkpub = publiser.objects.filter(pubid=pubid)
    if checkpub:
        obj = publiser.objects.get(pubid=pubid)
        pub = {
            'datapub': obj,
        }
        return render(request, 'Publisher/pubprofile.html', pub)


# Request of Advertisement
def advrequest(request):
    if request.method == "POST":
        form = AdvRequestForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.add_message(request, messages.INFO, 'Successfully Sent a Request For Booking Advertise')
                return render(request, "Advertiser/advertiserhome.html")
            except:
                pass
    else:
        form = AdvRequestForm()
    return render(request, 'index.html', {'form': form})


# Request Details at Advertiser site
def requestdtl(request):
    adverid = request.session.get("loginid")
    disreq = advRequest.objects.filter(adverid=adverid)
    if disreq:
        reqe = {
            'data': disreq,
        }
        return render(request, 'Advertiser/myrequest.html', reqe)
    else:
        return render(request, 'Advertiser/myrequest.html')


# Request Details at Publisher site
def requestdtlinpub(request):
    pubid = request.session.get("publogid")
    disreqinpub = advRequest.objects.filter(pubid=pubid)
    if disreqinpub:
        preq = {
            'data': disreqinpub,
        }
        return render(request, 'Publisher/requestpublisher.html', preq)
    else:
        return render(request, 'Publisher/requestpublisher.html')

def admin_dashboard(request):
    if 'admin_id' not in request.session:
        return redirect('admin_login')
    
'''def admin_dashboard(request):
    return render(request,"AdminHome/admin_dashboard.html")'''

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("admin_dashboard")
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "admin_login.html")

def admin_logout(request):
    request.session.flush()   # Clear session
    return redirect("admin_login")


def admin_dashboard(request):
    total_advertisers = advertiser.objects.count()
    total_publishers = publiser.objects.count()
    total_locations = SavLoc.objects.count()
    total_requests = advRequest.objects.count()

    latest_requests = advRequest.objects.all().order_by('-advrequestid')[:5]

    context = {
        'total_advertisers': total_advertisers,
        'total_publishers': total_publishers,
        'total_locations': total_locations,
        'total_requests': total_requests,
        'latest_requests': latest_requests,
    }
    return render(request, "AdminHome/admin_dashboard.html", context)

def admin_advertisers(request):
    data = advertiser.objects.all()
    return render(request, "AdminHome/admin_advertisers.html", {"data": data})

# UPDATE
def edit_advertiser(request, id):
    adv = get_object_or_404(advertiser, pk=id)
    if request.method == 'POST':
        adv.fname = request.POST['fname']
        adv.lname = request.POST['lname']
        adv.gender = request.POST['gender']
        adv.role = request.POST['role']
        adv.emailid = request.POST['emailid']
        adv.password = request.POST['password']
        adv.save()
        messages.success(request, "Advertiser updated successfully!")
        return redirect('admin_advertisers')
    return render(request, "AdminHome/advertiser_form.html", {'advertiser': adv})

# DELETE
def delete_advertiser(request, id):
    adv = get_object_or_404(advertiser, pk=id)
    adv.delete()
    messages.success(request, "Advertiser deleted successfully!")
    return redirect('admin_advertisers')

def admin_publishers(request):
    data = publiser.objects.all()
    return render(request, "AdminHome/admin_publishers.html", {"data": data})

# UPDATE
def edit_publisher(request, id):
    pub = get_object_or_404(publiser, pk=id)
    if request.method == 'POST':
        pub.fname = request.POST['fname']
        pub.lname = request.POST['lname']
        pub.cname = request.POST['cname']
        pub.addres1 = request.POST['addres1']
        pub.addres2 = request.POST['addres2']
        pub.emailid = request.POST['emailid']
        pub.role = request.POST['role']
        pub.password = request.POST['password']
        pub.save()
        messages.success(request, "Publisher updated successfully!")
        return redirect('admin_publishers')
    return render(request, "AdminHome/publisher_form.html", {'publisher': pub})

# DELETE
def delete_publisher(request, id):
    pub = get_object_or_404(publiser, pk=id)
    pub.delete()
    messages.success(request, "Publisher deleted successfully!")
    return redirect('admin_publishers')


def admin_locations(request):
    data = SavLoc.objects.all()
    return render(request, "AdminHome/admin_locations.html", {"data": data})

# UPDATE
def edit_location(request, id):
    loc = get_object_or_404(SavLoc, pk=id)
    if request.method == 'POST':
        loc.pubid = request.POST['pubid']
        if 'locimage' in request.FILES:
            loc.locimage = request.FILES['locimage']
        loc.locname = request.POST['locname']
        loc.locaddress = request.POST['locaddress']
        loc.pcname = request.POST['pcname']
        loc.contactno = request.POST['contactno']
        loc.parea = request.POST['parea']
        loc.city = request.POST['city']
        loc.adtype = request.POST['adtype']
        loc.noadv = request.POST['noadv']
        loc.advsize = request.POST['advsize']
        loc.advprice = request.POST['advprice']
        loc.save()
        messages.success(request, "Location updated successfully!")
        return redirect('admin_locations')
    return render(request, "AdminHome/location_form.html", {'location': loc})

# DELETE
def delete_location(request, id):
    loc = get_object_or_404(SavLoc, pk=id)
    loc.delete()
    messages.success(request, "Location deleted successfully!")
    return redirect('admin_locations')

def admin_requests(request):
    data = advRequest.objects.all()
    return render(request, "AdminHome/admin_requests.html", {"data": data})

# UPDATE
def edit_request(request, id):
    req = get_object_or_404(advRequest, pk=id)

    if request.method == 'POST':
        req.locaddress = request.POST['locaddress']
        req.parea = request.POST['parea']
        req.city = request.POST['city']
        req.adtype = request.POST['adtype']
        req.advsize = request.POST['advsize']
        req.advprice = request.POST['advprice']
        req.pubid = request.POST['pubid']
        req.locid = request.POST['locid']
        req.adverid = request.POST['adverid']
        req.fname = request.POST['fname']
        req.lname = request.POST['lname']
        req.cname = request.POST['cname']
        req.contactno = request.POST['contactno']
        req.starttime = request.POST['starttime']
        req.lastdate = request.POST['lastdate']
        req.save()

        messages.success(request, "Advertisement Request updated successfully!")
        return redirect('admin_requests')

    return render(request, "AdminHome/request_form.html", {'req': req})

# DELETE
def delete_request(request, id):
    req = get_object_or_404(advRequest, pk=id)
    req.delete()
    messages.success(request, "Advertisement Request deleted successfully!")
    return redirect('admin_requests')
