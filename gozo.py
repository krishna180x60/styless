from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_player import st_player
import webbrowser
#for emojis-> [ https://webfx.com/tools/emoji-cheat-sheet/ ]😼
st.set_page_config(page_title='gozo',page_icon="image/icon.png",layout="wide")

with st.container():
    left_column,centre_column,right_column=st.columns((1,3,1))
    with centre_column:
        head='''<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8440799604795585"
     crossorigin="anonymous"></script>'''
        st.markdown(head,unsafe_allow_html=True)
    with left_column:
        st.empty()
    with right_column:
        st.empty()

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css('style/style.css')
local_css('style/sharebutton.css')


#local js
def local_js(file_name):
    with open(file_name) as f:
        st.markdown(f"<script>{f.read()}</script",unsafe_allow_html=True)

# local_js("js/sharebutton.js")

#---load assets---
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/animated_stickers/lf_tgs_g7ve4rc8.json")
lottie_coding2 = load_lottieurl("https://assets1.lottiefiles.com/animated_stickers/lf_tgs_j7miwfxd.json")
lottie_shield = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_jvki4wd1.json")
lottie_fix = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_y6fnawnb.json")
img_header= Image.open("image/nameicon.png")
img_icon= Image.open("image/Iccon.png")
img_contact_form= Image.open("image/mcafee.png")
img_lottie_animation = Image.open("image/mcafee2.png")
img_contact_form2= Image.open("image/pubg.png")
#----header section----
with st.container():
    image_column,text_column,right_column=st.columns((1,3,1))
    with image_column:
        st.image(img_icon)
    with text_column:
        st.image(img_header)
    with right_column:
        st_lottie(lottie_coding2,height=200,key="codin")

    
    

with st.container():
     st.write("---")
     st.subheader(" こんにちは、みんな! :🙃: ")
     st.title(":red[Gozo]- The new site to watch/download anime online in hindi for free")
     st.write('''There is only few anime which are dubbed in hindi so we can't say. That we have big collection
                 However as time being passes we will add new anime as soon as when they get dubbed.''')
    #  st.write("[learn more >](https://gamegamesimsim.netlify.app/)")


     
     url = 'http://localhost:8501/Home'
 
     if st.button("Visit The FullSite"):
         webbrowser.open("https://gozoanime.world")
#---what i do----
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("SHARE GOZO")
        st.subheader("""with your comrades👇""")
        share_button=''' 
        
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <meta https-equiv="X-UA-Compatible" content="ie=edge" />
            <link rel="stylesheet" href="style.css" />
            <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans&display=swap" rel="stylesheet">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

            <div class="animated_share"> 
               <div class="animated_share_btn">
                 <a href="https://m.facebook.com/dialog/share?app_id=140586622674265&display=popup&href=https%3A%2F%2Fgozoanime.streamlit.app%2F%23.ZE9kpMK-hwM.facebook&redirect_uri=http%3A%2F%2Fs7.addthis.com%2Fstatic%2Fthankyou.html" target="_main"><i class="fa fa-facebook"></i></a>
                 <a href="https://www.reddit.com/submit?url=https%3A%2F%2Fhttp://gozoanime.streamlit.app%2Fquestions%2F24823114%2Fpost-to-reddit-via-url&title=Watch/Download%20Anime%20in%20hindi%20on%20Gozoanime->%20http://gozoanime.streamlit.app" target="_main"><i class="fa fa-reddit"></i></a>
                 <a href="https://twitter.com/intent/tweet?text=Watch/Download%20Anime%20in%20hindi%20on%20Gozoanime->%20http://gozoanime.streamlit.app" target="_main"><i class="fa fa-twitter"></i></a>
                 <a href="whatsapp://send?text=Watch/Download Anime in hindi on Gozoanime->http://gozoanime.streamlit.app"><i class="fa fa-whatsapp" target="_main"></i></a>
               </div>
           </div>
            
        
        '''    
        st.markdown(share_button,unsafe_allow_html=True)
    with right_column:
        st.empty()

        # st.write("[my other projects >](https://checkspot4.wordpress.com/)")
    with right_column:
        st_lottie(lottie_coding,height=210,key="coding")
    
#---projects--
with st.container():
     st.write("---")
     st.header(":blue[What] is :red[Gozoanime]?😎")
     st.write(
        """Gozoanime is a platform that helps you to watch/Download anime in hindi. for free without any ads
           This is just a experiment site. so it doesn't contain any professional term. This site is Underdeveloping 
           In future it will be better.

        
        """)
     st.subheader("Watch Anime in Hindi without any problem")
with st.container():

    # st.markdown("[play](https://video.bunnycdn.com/play/118812/0ecf2a7e-9243-48a8-b037-63ba04342f8f)")
    st.write("---")
    st.header(":green[-----Is it Safe🛡?-----]")
    # st.write("##")
    left_column,text_column=st.columns((1,2))
    with left_column:
        #insert image
        st_lottie(lottie_shield,height=225,key="codi")
    with text_column:
        st.subheader("This website do not require any login.")
        st.write(
            '''
             you can access the website without any ads or login so your data will be :green[safe]
             however but download and Videoplayer section contain some ads to cover up the server cost.\n
                :)
            '''
        )
        # st.markdown("[watch video...](https://youtu.be/mwB0PJKMtT8)")
    # st_player("https://video.bunnycdn.com/play/118812/0ecf2a7e-9243-48a8-b037-63ba04342f8f")
    
with st.container():
    st.header("chainsaw man ep1 in hindi")
    st_player("https://video.bunnycdn.com/play/118823/5c7dea31-578b-43be-afab-68e7831245c3")


with st.container():
    st.write("---")
    st.header(":red[-----If website not working, what should i do🤕?-----]")
    left_column,text_column = st.columns((1,2))
    with left_column:
        st_lottie(lottie_fix,height=225,key="cod")
    with text_column:
        st.subheader("Refresh it or try using chrome,firefox browsers")
        st.write(
            '''
            This problem may be occuring from the server error or while updateing or changing or uploading can cause the site crash
            if any error occur it will take time to fix.

            '''
        )
        # st.markdown("[watch video...](https://youtu.be/wWR4rKhI_Hs)")
       
#---contact---
with st.container():
    st.write("---")
    st.header("leave a suggestion")
    st.write("##")

    #documentation https://formsubmit.co/  !change email address
    contact_form= '''
    <form action="https://formsubmit.co/divinexdeo2003@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder= "Your Name" required>
        <input type="email" name="email" placeholder= "Your Email" required>
        <textarea name="message" placeholder= "Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    '''
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()
