from django.core.mail import send_mail

from courses.models import Courses


def registration_successful(user):
    latest_course = Courses.objects.filter(isPublished=True).order_by('-createdAt')[:3]
    code_template = f'''
    <!DOCTYPE html>
<html lang="en">
<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bellota:ital,wght@0,300;0,400;0,700;1,300;1,400;1,700&family=Philosopher:ital,wght@0,400;0,700;1,400;1,700&display=swap" rel="stylesheet">
    <title>Unique Accent Email</title>
</head>
<body style="background: #d9d9d9; font-family: 'Bellota', cursive;">
    <a href="https://uniqueaccent.com.ng/" style="display: grid; justify-content: center; padding: 20px">
        <img style="width: 15vw" src="https://uniqueaccent.com.ng/assets/UACLLogo.png" alt="Unique Accent" >
    </a>
    <hr>
    <div style="font-size: 1.3em; display: grid; gap: 20px; padding: 40px">
        <div>Hi {user.name},</div>
        <div>Welcome to the Unique Family.</div>
        <div>We are delighted to inform you that you've completed your registration with <strong>Unique Accent Consultancy Limited</strong>.</div>
        <div>
            <a href="https://uniqueaccent.com.ng/auth/login">Click here to login to your account</a>
        </div>
    </div>
    <div style="background: #FF6600; text-align: center">
        <h1 style="font-family: 'Philosopher', sans-serif;">Latest Courses</h1>
        <div style="display: flex; justify-content: center; flex-wrap: wrap; padding: 10px; gap: 20px">
        '''
    for course in latest_course:
        code_template = code_template + f'''<div style="max-width: 300px; background: #f1f1f1; box-shadow: 0 0 10px #f1f1f1; border-radius: 10px; padding: 10px; text-align: center">
                <img style="height: 150px; margin: auto; display: block" src="{course.thumbnail}" alt="courseimage">
                <div class="coursedetails">
                    <h3 style="font-family: 'Philosopher', sans-serif;">{course.title}</h3>
                    <p>{course.description}</p>
                </div>
                <a href="https://uniqueaccent.com.ng/courses/{course.slug}" style="display: block; text-decoration: none; background: #FF6600; border: none; border-radius: 10px; padding: 10px; cursor: pointer; color: #f1f1f1">View Couurse</button>
            </div>'''
    code_template = code_template + '''
        </div>
    </div>

  <footer style="background: #000000; color: white; display: grid; justify-content: center; text-align: center; font-size: 1.2em; gap: 10px; padding: 20px">
    <div>Unique Accent Consultancy Limited</div>
    <div>57 Ago Palace Way, Okota, Lagos</div>
    <div>
        <a href="tel:+2348034802475" style="color: inherit; text-decoration: none">+234 803 480 2475</a>
        <a href="tel:+2347032767180" style="color: inherit; text-decoration: none">+234 703 276 7180</a>
    </div>
    <div>
        <a href="mailto:info@uniqueaccent.com.ng" style="color: inherit; text-decoration: none">info@uniqueaccent.com.ng</a>
    </div>
    <div style="display: flex; align-items: center; justify-content: center; gap: 50px; margin: 20px">
        <a href="" style="color: #aeaeae">
            <svg style="width: 50px" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="facebook" class="svg-inline--fa fa-facebook fa-w-16" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path fill="currentColor" d="M504 256C504 119 393 8 256 8S8 119 8 256c0 123.78 90.69 226.38 209.25 245V327.69h-63V256h63v-54.64c0-62.15 37-96.48 93.67-96.48 27.14 0 55.52 4.84 55.52 4.84v61h-31.28c-30.8 0-40.41 19.12-40.41 38.73V256h68.78l-11 71.69h-57.78V501C413.31 482.38 504 379.78 504 256z"></path></svg>
        </a>

        <a href="" style="color: #aeaeae">
            <svg style="width: 50px" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="instagram" class="svg-inline--fa fa-instagram fa-w-14" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path fill="currentColor" d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z"></path></svg>
        </a>

        <a href="" style="color: #aeaeae">
            <svg style="width: 50px" aria-hidden="true" focusable="false" data-prefix="fab" data-icon="youtube" class="svg-inline--fa fa-youtube fa-w-18" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path fill="currentColor" d="M549.655 124.083c-6.281-23.65-24.787-42.276-48.284-48.597C458.781 64 288 64 288 64S117.22 64 74.629 75.486c-23.497 6.322-42.003 24.947-48.284 48.597-11.412 42.867-11.412 132.305-11.412 132.305s0 89.438 11.412 132.305c6.281 23.65 24.787 41.5 48.284 47.821C117.22 448 288 448 288 448s170.78 0 213.371-11.486c23.497-6.321 42.003-24.171 48.284-47.821 11.412-42.867 11.412-132.305 11.412-132.305s0-89.438-11.412-132.305zm-317.51 213.508V175.185l142.739 81.205-142.739 81.201z"></path></svg>
        </a>
    </div>
</footer>

</body>
</html>
    '''
    return code_template


def send_purchase_confirmation(user_name, user_email, product_name):
    return f'''<div style="background-color:#ffffff;background-position:top;background-image:url('https://ci5.googleusercontent.com/proxy/qqN6grZKTiVXosze0-u3xZP_bKNaVVvXgSZAITMtFlibWxuMKCpI2xoiIfbQ8uJsYGDjoRkpgMNJyrfVoZJWMfI06j0iNt4NXSwr6xomedfKNmO-NeKWKCzP1RSTCX3a21Aj=s0-d-e1-ft#https://d1pgqke3goo8l6.cloudfront.net/vr3GE0A4T72rPF3Sh5II_dys-bg-blue-clear.png');background-repeat:no-repeat">


   <div style="margin:0px auto;max-width:600px">
    <table align="center" border="0" cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse">
     <tbody>
      <tr>
       <td style="direction:ltr;font-size:0px;padding:20px 0px;text-align:center;vertical-align:top;border-collapse:collapse;border:0px">

        <div style="direction:ltr;display:inline-block;font-size:13px;text-align:left;vertical-align:top;width:100%">
         <table border="0" cellpadding="0" cellspacing="0" style="vertical-align:top;border-collapse:collapse" width="100%">
          <tbody>
           <tr>
            <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;border-collapse:collapse;border:0px">
             <table border="0" cellpadding="0" cellspacing="0" style="border-collapse:collapse;border-spacing:0px">
              <tbody>
               <tr>
                <td style="width:120px;border-collapse:collapse;border:0px"><a href="https://uniqueaccent.com.ng"><img alt="Unique Accent Logo" height="auto" src="https://uniqueaccent.com.ng/assets/UACLLogo.png" style="border:none;display:block;font-size:13px;height:auto;outline:none;text-decoration:none;width:100%;line-height:100%" width="200" class="CToWUd"></a></td>
               </tr>
              </tbody>
             </table> </td>
           </tr>
          </tbody>
         </table>
        </div>
        </td>
      </tr>
     </tbody>
    </table>
   </div>




   <div style="background:#ffffff;background-color:#ffffff;margin:0px auto;max-width:600px">
    <table align="center" border="0" cellpadding="0" cellspacing="0" style="background:rgb(255,255,255);width:100%;border-collapse:collapse">
     <tbody>
      <tr>
       <td style="border-width:1px 1px 0px;border-top-style:solid;border-right-style:solid;border-left-style:solid;border-top-color:rgb(222,235,250);border-right-color:rgb(222,235,250);border-left-color:rgb(222,235,250);border-bottom-style:initial;border-bottom-color:initial;direction:ltr;font-size:0px;padding:15px;text-align:center;vertical-align:top;border-collapse:collapse">

        <div style="direction:ltr;display:inline-block;font-size:13px;text-align:left;vertical-align:top;width:100%">
         <table border="0" cellpadding="0" cellspacing="0" style="vertical-align:top;border-collapse:collapse" width="100%"></table>
        </div>
        </td>
      </tr>
     </tbody>
    </table>
   </div>


   <div style="background:#ffffff;background-color:#ffffff;margin:0px auto;max-width:600px">
    <table align="center" border="0" cellpadding="0" cellspacing="0" style="background:rgb(255,255,255);width:100%;border-collapse:collapse">
     <tbody>
      <tr>
       <td style="border-width:0px 1px;border-right-style:solid;border-left-style:solid;border-right-color:rgb(222,235,250);border-left-color:rgb(222,235,250);border-bottom-style:initial;border-bottom-color:initial;border-top-style:initial;border-top-color:initial;direction:ltr;font-size:0px;padding:15px;text-align:center;vertical-align:top;border-collapse:collapse">

        <div style="direction:ltr;display:inline-block;font-size:13px;text-align:left;vertical-align:top;width:100%">
         <table border="0" cellpadding="0" cellspacing="0" style="vertical-align:top;border-collapse:collapse" width="100%">
          <tbody>
           <tr>
            <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;border-collapse:collapse;border:0px">
             <div style="color:#3d3d3d;font-family:Lato,Helvetica,Arial,sans-serif;font-size:16px;line-height:1.6;text-align:left">
              <p style="margin:0px;display:block">Hello {user_name},<br> <br> Thanks for purchasing {product_name}. My name is Dylan and as the Head of Customer Success, I'm reaching out to introduce myself as an additional resource and will help as a trial coach over the next week.</p>
              <p style="margin:0px;display:block"><br> We have found that all successful trials have one thing in common, they let us help with the first template import. If you’d like to send us one of your existing templates, my team would be happy to do the heavy lifting so that you can jump straight into the email builder, where the true value of Dyspatch really shines. To send us your template, just reply to this email.</p>
              <p style="margin:0px;display:block"><br></p>
              <p style="margin:0px;display:block">Interested in a customized demo? - <a href="http://fmtrack1.dyspatch.io/ls/click?upn=5EPtVKcEsZTOl0ymYbTSSt6bBmPavFQW770kxvG57IyCoNU6D4QkH2GbY0WzW-2FA2wBgqQRAduhAi4KOKgetczo4CkxJCfdYee1M7Y8HXb70XNIwbKHSO1TB7kznrq7S5tlxfQQ-2BBxVb6LoRjaNSj7jK-2B2ckBCjHNaDdZeziJpQh7-2FUTpIeJAfDMiZQMYk6kzl4fF4qTQ3ocTFsqnYewUlocgpi6LsyYklLGzxspCm7Id-2FAwbqS9lagvIS35Eis4ujp0UqJ0svat7qdKbnOkrizP8phgcWQ1eGGlfiyYmCOCYpnjXw48Fs0CT-2B4DW76J9blzG_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU57BtBDJte7ZQQUraUolJ-2BQPNMhlLh-2FY1Zq1Qxvh5VzTnDl-2FdXCWPWapC9MhznVISv94aTASmon7-2BkkBn5lKXjO1A0R5EEke-2BOuvlRtMVcB-2BJVBaP2ZgsRunoKENtMcyIckqxfAQPI-2Bf-2BxxwSxKoLshqvruyUFd1LUz2tljbVDv5" style="color:rgb(69,143,221);text-decoration:underline" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://fmtrack1.dyspatch.io/ls/click?upn%3D5EPtVKcEsZTOl0ymYbTSSt6bBmPavFQW770kxvG57IyCoNU6D4QkH2GbY0WzW-2FA2wBgqQRAduhAi4KOKgetczo4CkxJCfdYee1M7Y8HXb70XNIwbKHSO1TB7kznrq7S5tlxfQQ-2BBxVb6LoRjaNSj7jK-2B2ckBCjHNaDdZeziJpQh7-2FUTpIeJAfDMiZQMYk6kzl4fF4qTQ3ocTFsqnYewUlocgpi6LsyYklLGzxspCm7Id-2FAwbqS9lagvIS35Eis4ujp0UqJ0svat7qdKbnOkrizP8phgcWQ1eGGlfiyYmCOCYpnjXw48Fs0CT-2B4DW76J9blzG_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU57BtBDJte7ZQQUraUolJ-2BQPNMhlLh-2FY1Zq1Qxvh5VzTnDl-2FdXCWPWapC9MhznVISv94aTASmon7-2BkkBn5lKXjO1A0R5EEke-2BOuvlRtMVcB-2BJVBaP2ZgsRunoKENtMcyIckqxfAQPI-2Bf-2BxxwSxKoLshqvruyUFd1LUz2tljbVDv5&amp;source=gmail&amp;ust=1624861275723000&amp;usg=AFQjCNGsw5rnM1vgM9h3pV-wAVM2GPyRoA">Book it here with our sales team</a>.</p>
              <p style="margin:0px;display:block"><br> If you have any questions, feel free to respond to this email.</p>
              <p style="margin:0px;display:block"><br> Thanks,<br> </p>
             </div> </td>
           </tr>
          </tbody>
         </table>
        </div>
        </td>
      </tr>
     </tbody>
    </table>
   </div>


   <div style="background:#ffffff;background-color:#ffffff;margin:0px auto;max-width:600px">
    <table align="center" border="0" cellpadding="0" cellspacing="0" style="background:rgb(255,255,255);width:100%;border-collapse:collapse">
     <tbody>
      <tr>
       <td style="border-width:0px 1px;border-right-style:solid;border-left-style:solid;border-right-color:rgb(222,235,250);border-left-color:rgb(222,235,250);border-bottom-style:initial;border-bottom-color:initial;border-top-style:initial;border-top-color:initial;direction:ltr;font-size:0px;padding:0px 15px;text-align:center;vertical-align:top;border-collapse:collapse">

        <div style="direction:ltr;display:inline-block;font-size:13px;text-align:left;vertical-align:top;width:100%">
         <table border="0" cellpadding="0" cellspacing="0" style="vertical-align:top;border-collapse:collapse" width="100%">
          <tbody>
           <tr>
            <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;border-collapse:collapse;border:0px">
             <table border="0" cellpadding="0" cellspacing="0" style="border-collapse:separate;line-height:100%">
              <tbody>
               <tr>
                <td align="center" bgcolor="#458fdd" style="background:rgb(69,143,221);border-width:0px 0px 2px;border-bottom-style:solid;border-bottom-color:rgb(5,92,184);border-left-style:initial;border-left-color:initial;border-radius:5px;border-right-style:initial;border-right-color:initial;border-top-style:initial;border-top-color:initial;border-collapse:collapse" valign="middle"><a href="http://fmtrack1.dyspatch.io/ls/click?upn=5EPtVKcEsZTOl0ymYbTSSt6bBmPavFQW770kxvG57IyCoNU6D4QkH2GbY0WzW-2FA2wBgqQRAduhAi4KOKgetczo4CkxJCfdYee1M7Y8HXb70XNIwbKHSO1TB7kznrq7S5tlxfQQ-2BBxVb6LoRjaNSj7jK-2B2ckBCjHNaDdZeziJpQh7-2FUTpIeJAfDMiZQMYk6kzl4fF4qTQ3ocTFsqnYewUlocgpi6LsyYklLGzxspCm7Id-2FAwbqS9lagvIS35Eis4ujp0UqJ0svat7qdKbnOkrizP8phgcWQ1eGGlfiyYmCOCYpnjXw48Fs0CT-2B4DW76J975ug_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU9Wy1aFehobiYwZD3ZqT7Nhby1HR0mYJD5YxrnOALI-2BjpPpIJcUw8JJfI3rkkttCH-2F2fNAhyqr-2FV-2Fzvp01Z0uyAW3qWNEaq2GSHtSqvvIMYIJ7Q2VifNOPoTZ2-2FGVdd9q2RU9FsYMlSxjg0KRrt3jac2t4L-2FDCHspzEeXjrdH3IK" style="background:rgb(69,143,221);border-radius:5px;color:rgb(255,255,255);display:inline-block;font-family:Helvetica,Arial,sans-serif;font-size:20px;line-height:120%;margin:0px;padding:15px 30px 12px;text-decoration:none;text-transform:none" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://fmtrack1.dyspatch.io/ls/click?upn%3D5EPtVKcEsZTOl0ymYbTSSt6bBmPavFQW770kxvG57IyCoNU6D4QkH2GbY0WzW-2FA2wBgqQRAduhAi4KOKgetczo4CkxJCfdYee1M7Y8HXb70XNIwbKHSO1TB7kznrq7S5tlxfQQ-2BBxVb6LoRjaNSj7jK-2B2ckBCjHNaDdZeziJpQh7-2FUTpIeJAfDMiZQMYk6kzl4fF4qTQ3ocTFsqnYewUlocgpi6LsyYklLGzxspCm7Id-2FAwbqS9lagvIS35Eis4ujp0UqJ0svat7qdKbnOkrizP8phgcWQ1eGGlfiyYmCOCYpnjXw48Fs0CT-2B4DW76J975ug_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU9Wy1aFehobiYwZD3ZqT7Nhby1HR0mYJD5YxrnOALI-2BjpPpIJcUw8JJfI3rkkttCH-2F2fNAhyqr-2FV-2Fzvp01Z0uyAW3qWNEaq2GSHtSqvvIMYIJ7Q2VifNOPoTZ2-2FGVdd9q2RU9FsYMlSxjg0KRrt3jac2t4L-2FDCHspzEeXjrdH3IK&amp;source=gmail&amp;ust=1624861275723000&amp;usg=AFQjCNGNCJXXkOenixld48deO-7EOWpO_g">Book a Call</a></td>
               </tr>
              </tbody>
             </table> </td>
           </tr>
          </tbody>
         </table>
        </div>
        </td>
      </tr>
     </tbody>
    </table>
   </div>


   <div style="background:#ffffff;background-color:#ffffff;margin:0px auto;max-width:600px">
    <table align="center" border="0" cellpadding="0" cellspacing="0" style="background:rgb(255,255,255);width:100%;border-collapse:collapse">
     <tbody>
      <tr>
       <td style="border-width:0px 1px;border-right-style:solid;border-left-style:solid;border-right-color:rgb(222,235,250);border-left-color:rgb(222,235,250);border-bottom-style:initial;border-bottom-color:initial;border-top-style:initial;border-top-color:initial;direction:ltr;font-size:0px;padding:15px;text-align:center;vertical-align:top;border-collapse:collapse">

        <div style="direction:ltr;display:inline-block;font-size:13px;text-align:left;vertical-align:top;width:100%">
         <table border="0" cellpadding="0" cellspacing="0" style="vertical-align:top;border-collapse:collapse" width="100%">
          <tbody>
           <tr>
            <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;border-collapse:collapse;border:0px">
             <div style="color:#3d3d3d;font-family:Lato,Helvetica,Arial,sans-serif;font-size:16px;line-height:1.6;text-align:left">
              <p style="margin:0px;display:block">Should you want to poke around on your own feel free to reference our <a href="http://fmtrack1.dyspatch.io/ls/click?upn=5EPtVKcEsZTOl0ymYbTSSiFp1ulgzfJii5-2BBy67bqDIH-2Fa4tNcz6RloyEnkaNT5oMSp4LUfVVP9fIZ3XkeopVzVuDjNezbHYmdasS4fEN5j7DjLRgSdg9sT4pPx5XY4EudxoGuAaOHaIY4IWxTCAix-2B8qoRozdpPmJ7sjKatySGvgLLAvOHpi3hjdTAWk62pdV0-2FhV-2BCPaXzC20xzBDUkkMzrl-2BoZtNiaL8Nc4UMbpdH4SrEEyU-2BDQSjpO41yt-2FnsCPvYYKrzQ5k4eIyY-2F-2FqHGZGcL6QT0uVfXIP-2BNdktbw-3DJALF_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU5211f50mFwiJQRCmM2H9QGjW5iucs51ynOTYmS28VKAEbfUjIn8NT83QNyLpGlZ7ITzxxmbL16QP-2FQ0yI-2FllkiQcqK8hmgsV4OYxisnYlGa9Pjl2T-2BXkMUBpSz9fggi-2FG0kGvH1qhvJ8C2sxFIw-2FSiyVEO9jiLTRyeHTQfw1mJ7" style="color:rgb(69,143,221);text-decoration:underline" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://fmtrack1.dyspatch.io/ls/click?upn%3D5EPtVKcEsZTOl0ymYbTSSiFp1ulgzfJii5-2BBy67bqDIH-2Fa4tNcz6RloyEnkaNT5oMSp4LUfVVP9fIZ3XkeopVzVuDjNezbHYmdasS4fEN5j7DjLRgSdg9sT4pPx5XY4EudxoGuAaOHaIY4IWxTCAix-2B8qoRozdpPmJ7sjKatySGvgLLAvOHpi3hjdTAWk62pdV0-2FhV-2BCPaXzC20xzBDUkkMzrl-2BoZtNiaL8Nc4UMbpdH4SrEEyU-2BDQSjpO41yt-2FnsCPvYYKrzQ5k4eIyY-2F-2FqHGZGcL6QT0uVfXIP-2BNdktbw-3DJALF_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU5211f50mFwiJQRCmM2H9QGjW5iucs51ynOTYmS28VKAEbfUjIn8NT83QNyLpGlZ7ITzxxmbL16QP-2FQ0yI-2FllkiQcqK8hmgsV4OYxisnYlGa9Pjl2T-2BXkMUBpSz9fggi-2FG0kGvH1qhvJ8C2sxFIw-2FSiyVEO9jiLTRyeHTQfw1mJ7&amp;source=gmail&amp;ust=1624861275723000&amp;usg=AFQjCNGuljrXIWYS9uaW9NSh-AhDo_WSkg">knowledge base</a>.</p>
             </div> </td>
           </tr>
          </tbody>
         </table>
        </div>
        </td>
      </tr>
     </tbody>
    </table>
   </div>


   <div style="background:#ffffff;background-color:#ffffff;margin:0px auto;max-width:600px">
    <table align="center" border="0" cellpadding="0" cellspacing="0" style="background:rgb(255,255,255);width:100%;border-collapse:collapse">
     <tbody>
      <tr>
       <td style="border-width:0px 1px;border-right-style:solid;border-left-style:solid;border-right-color:rgb(222,235,250);border-left-color:rgb(222,235,250);border-bottom-style:initial;border-bottom-color:initial;border-top-style:initial;border-top-color:initial;direction:ltr;font-size:0px;padding:0px 25px 25px;text-align:center;vertical-align:top;border-collapse:collapse">

        <div style="direction:ltr;display:inline-block;font-size:0;line-height:0;text-align:left;width:100%">


         <div style="direction:ltr;display:inline-block;font-size:13px;text-align:left;vertical-align:top;width:15%">
          <table border="0" cellpadding="0" cellspacing="0" style="border-collapse:collapse" width="100%">
           <tbody>
            <tr>
             <td style="padding-right:0px;vertical-align:top;border-collapse:collapse;border:0px">
              <table border="0" cellpadding="0" cellspacing="0" style="border-collapse:collapse" width="100%">
               <tbody>
                <tr>
                 <td align="left" style="font-size:0px;padding:0px;word-break:break-word;border-collapse:collapse;border:0px">
                  <table border="0" cellpadding="0" cellspacing="0" style="border-collapse:collapse;border-spacing:0px">
                   <tbody>
                    <tr>
                     <td style="width:90px;border-collapse:collapse;border:0px"><img alt="Dylan Moore Profile Image" height="auto" src="https://ci5.googleusercontent.com/proxy/rR6cnx6w_cD7up8sQOZ7TxuO6Yw72uqhaB9y7qvDVM_5-FQl0-zKobrY7ojhdtilr86-7tw-Nx4zbqGSc98QqBDupfhqY_zr1NufKML2nmL5LBnKv3d9=s0-d-e1-ft#https://d1pgqke3goo8l6.cloudfront.net/dhTOLW0tRSSjDErNhAy1_dylan.png" style="border:none;display:block;font-size:13px;height:auto;outline:none;text-decoration:none;width:100%;line-height:100%" width="90" class="CToWUd"></td>
                    </tr>
                   </tbody>
                  </table> </td>
                </tr>
               </tbody>
              </table> </td>
            </tr>
           </tbody>
          </table>
         </div>

         <div style="direction:ltr;display:inline-block;font-size:13px;text-align:left;vertical-align:top;width:85%">
          <table border="0" cellpadding="0" cellspacing="0" style="border-collapse:collapse" width="100%">
           <tbody>
            <tr>
             <td style="padding-left:0px;vertical-align:top;border-collapse:collapse;border:0px">
              <table border="0" cellpadding="0" cellspacing="0" style="border-collapse:collapse" width="100%">
               <tbody>
                <tr>
                 <td align="left" style="font-size:0px;padding:10px 25px;word-break:break-word;border-collapse:collapse;border:0px">
                  <div style="color:#3d3d3d;font-family:Lato,Helvetica,Arial,sans-serif;font-size:16px;line-height:18px;text-align:left">
                   <span style="font-size:20px"><strong>Dylan Moore</strong></span>
                   <br>
                   <span style="color:#999;font-size:13px"><em>Director of Customer Success</em></span>
                   <br>
                   <a href="mailto:dylan@dyspatch.io" style="color:rgb(153,153,153);font-size:13px;text-decoration:underline" target="_blank">dylan@dyspatch.io</a>
                  </div> </td>
                </tr>
               </tbody>
              </table> </td>
            </tr>
           </tbody>
          </table>
         </div>


        </div>
        </td>
      </tr>
     </tbody>
    </table>
   </div>


   <div style="background:#ffffff;background-color:#ffffff;margin:0px auto;max-width:600px">
    <table align="center" border="0" cellpadding="0" cellspacing="0" style="background:rgb(255,255,255);width:100%;border-collapse:collapse">
     <tbody>
      <tr>
       <td style="border-width:0px 1px 1px;border-right-style:solid;border-bottom-style:solid;border-left-style:solid;border-right-color:rgb(222,235,250);border-bottom-color:rgb(222,235,250);border-left-color:rgb(222,235,250);border-top-style:initial;border-top-color:initial;direction:ltr;font-size:0px;padding:15px;text-align:center;vertical-align:top;border-collapse:collapse">

        <div style="direction:ltr;display:inline-block;font-size:13px;text-align:left;vertical-align:top;width:100%">
         <table border="0" cellpadding="0" cellspacing="0" style="vertical-align:top;border-collapse:collapse" width="100%"></table>
        </div>
        </td>
      </tr>
     </tbody>
    </table>
   </div>


   <div style="margin:0px auto;max-width:600px">
    <table align="center" border="0" cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse">
     <tbody>
      <tr>
       <td style="direction:ltr;font-size:0px;padding:0px;text-align:center;vertical-align:top;border-collapse:collapse;border:0px">

        <div style="direction:ltr;display:inline-block;font-size:13px;text-align:left;vertical-align:top;width:100%">
         <table border="0" cellpadding="0" cellspacing="0" style="border-collapse:collapse" width="100%">
          <tbody>
           <tr>
            <td style="padding:0px;vertical-align:top;border-collapse:collapse;border:0px">
             <table border="0" cellpadding="0" cellspacing="0" style="border-collapse:collapse" width="100%">
              <tbody>
               <tr>
                <td align="center" style="font-size:0px;padding:0px;word-break:break-word;border-collapse:collapse;border:0px">
                 <table border="0" cellpadding="0" cellspacing="0" style="border-collapse:collapse;border-spacing:0px">
                  <tbody>
                   <tr>
                    <td style="width:600px;border-collapse:collapse;border:0px"><img alt="Divider" height="auto" src="https://ci4.googleusercontent.com/proxy/s2UDsbWAJqFv-uGojinFnUTQWHd_iuHu2OYqqXh1hXasFgVMKg1IvMHzwD8aACvDpzZt0c02mTwCWqXtJ_YJyzAEoRlRFlWXIgJl2oV_N-6mp5v68TPZC-Hfdq0AqCn0Z3tDpRcL=s0-d-e1-ft#https://d1pgqke3goo8l6.cloudfront.net/JscEszaPQc6ApsX091GE_shadow-bottom%20copy.png" style="border:none;display:block;font-size:13px;height:auto;outline:none;text-decoration:none;width:100%;line-height:100%" width="600" class="CToWUd"></td>
                   </tr>
                  </tbody>
                 </table> </td>
               </tr>
              </tbody>
             </table> </td>
           </tr>
          </tbody>
         </table>
        </div>
        </td>
      </tr>
     </tbody>
    </table>
   </div>


   <div style="margin:0px auto;max-width:600px">
    <table align="center" border="0" cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse">
     <tbody>
      <tr>
       <td style="direction:ltr;font-size:0px;padding:20px 0px;text-align:center;vertical-align:top;border-collapse:collapse;border:0px">

        <div style="direction:ltr;display:inline-block;font-size:13px;text-align:left;vertical-align:top;width:100%">
         <table border="0" cellpadding="0" cellspacing="0" style="vertical-align:top;border-collapse:collapse" width="100%">
          <tbody>
           <tr>
            <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;border-collapse:collapse;border:0px">
             <table border="0" cellpadding="0" cellspacing="0" style="border-collapse:collapse;border-spacing:0px">
              <tbody>
               <tr>
                <td style="width:75px;border-collapse:collapse;border:0px"><a href="http://fmtrack1.dyspatch.io/ls/click?upn=5EPtVKcEsZTOl0ymYbTSSt6bBmPavFQW770kxvG57IzokNVZMpTu4-2Frhwz9F-2BZC3c84S9qCuT-2Fhj-2FYlDHCmy-2BXT-2FmTzVsVfofJH-2F-2BFsjkJwrwocN73SAqKO4arWB81MFL-2Bszd4RG2IWtlDgVFDQJXpngJyKEBjdSk5ysVZKDF0mi8fpNujOxqvs5N82afLxIYap44ZZ-2FS8odHhSsPAEHk6FE7q5YblbcvaPDSQNr4iLyEljlfB84kFjNDpQoG1lhW6mNpxH2Pl0xutXyPwtvyxHLsusDR2UrfWtpP-2BodHhw-3DTIDG_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU0Y13GMuFF1lO2zOuvmgU1eNQ-2FoeVcYD8P44l-2FU-2FQQnux5z5cnFTXx-2F37ou6OVAsPE43yZ7wSZfieCj-2FsZVCeSZwKpTiNWcvxiVtxdxns0GBQFN3JRT2w7ZkwqZ1xV2D3400nbh0h74P10cI21hSTpFagxAwOpMBGT3Esbvz-2BrXi" style="color:rgb(69,143,221);text-decoration:underline" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://fmtrack1.dyspatch.io/ls/click?upn%3D5EPtVKcEsZTOl0ymYbTSSt6bBmPavFQW770kxvG57IzokNVZMpTu4-2Frhwz9F-2BZC3c84S9qCuT-2Fhj-2FYlDHCmy-2BXT-2FmTzVsVfofJH-2F-2BFsjkJwrwocN73SAqKO4arWB81MFL-2Bszd4RG2IWtlDgVFDQJXpngJyKEBjdSk5ysVZKDF0mi8fpNujOxqvs5N82afLxIYap44ZZ-2FS8odHhSsPAEHk6FE7q5YblbcvaPDSQNr4iLyEljlfB84kFjNDpQoG1lhW6mNpxH2Pl0xutXyPwtvyxHLsusDR2UrfWtpP-2BodHhw-3DTIDG_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU0Y13GMuFF1lO2zOuvmgU1eNQ-2FoeVcYD8P44l-2FU-2FQQnux5z5cnFTXx-2F37ou6OVAsPE43yZ7wSZfieCj-2FsZVCeSZwKpTiNWcvxiVtxdxns0GBQFN3JRT2w7ZkwqZ1xV2D3400nbh0h74P10cI21hSTpFagxAwOpMBGT3Esbvz-2BrXi&amp;source=gmail&amp;ust=1624861275724000&amp;usg=AFQjCNHrq9EgvuT4z6dgm-0J-eiRCU108A"><img alt="Dyspatch Icon" height="auto" src="https://ci4.googleusercontent.com/proxy/dqZHzCAhtIrKHs_vXToUuSxSFUDI7Zwo17PBVDwcVQmzq9Qmy3SFyPbEvdJCrPJ9pLDM_RzkduCQNyq0ErYWc0i_NCl8C0_-EI_4fP203EGSrSpRpupN9CwIuPb08oL_=s0-d-e1-ft#https://d1pgqke3goo8l6.cloudfront.net/Jjfdhsi4TvG7Z2grpeSu_dys-icon-email.png" style="border:none;display:block;font-size:13px;height:auto;outline:none;text-decoration:none;width:100%;vertical-align:top;margin:5px auto;text-align:center;line-height:100%" width="75" class="CToWUd"></a></td>
               </tr>
              </tbody>
             </table> </td>
           </tr>
          </tbody>
         </table>
        </div>
        </td>
      </tr>
     </tbody>
    </table>
   </div>

   <center>
    <a href="http://fmtrack1.dyspatch.io/ls/click?upn=5EPtVKcEsZTOl0ymYbTSSqVJ5WepAaZpCrWcwLOc6e-2BJC099fVyDv-2FB9MdclMfjTPUMzsDwms-2FAcp6DdWDphpHFxenqsLmcOdiWCeeWllBC-2BBGRDbopEVrO4V8yWc5-2FA0cnq8kXK1y2eigaYQigYRgzUoCrmnA3C1laH1q2HZP-2Ftoli3mAHzrV9iR-2FH2q-2F8CbwD3NPQOBL8rEU29pO57sFGsIqh37LQjr62jOfSni-2BpQE92A155Bty2YWh-2BIhPKGEPYgiSxqU4blcx72-2By9kBgOdMr6-2FZ4Yq7Jk-2BWLI4-2BMq-2Bw0QsmVd3MCRT1NMfevQ1Vc6X_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU6oJpQ-2FNnQOeLR8-2FLd8UOxLr5POtSvbJO073x4Dhs-2BVn6cfU1O2Fu4znPMrjrmou7zK-2B7aFUOwwNcZGuWdP4EPgDUY96g9v5aXXNnhn-2BX8hItBHdA4zoFGTRRZIfkXYdNHYr0kFdZkQ7lwAxYztVkhdRsK7hWUdWlNgDTps6EI20" style="text-decoration:none;color:rgb(69,143,221)" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://fmtrack1.dyspatch.io/ls/click?upn%3D5EPtVKcEsZTOl0ymYbTSSqVJ5WepAaZpCrWcwLOc6e-2BJC099fVyDv-2FB9MdclMfjTPUMzsDwms-2FAcp6DdWDphpHFxenqsLmcOdiWCeeWllBC-2BBGRDbopEVrO4V8yWc5-2FA0cnq8kXK1y2eigaYQigYRgzUoCrmnA3C1laH1q2HZP-2Ftoli3mAHzrV9iR-2FH2q-2F8CbwD3NPQOBL8rEU29pO57sFGsIqh37LQjr62jOfSni-2BpQE92A155Bty2YWh-2BIhPKGEPYgiSxqU4blcx72-2By9kBgOdMr6-2FZ4Yq7Jk-2BWLI4-2BMq-2Bw0QsmVd3MCRT1NMfevQ1Vc6X_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU6oJpQ-2FNnQOeLR8-2FLd8UOxLr5POtSvbJO073x4Dhs-2BVn6cfU1O2Fu4znPMrjrmou7zK-2B7aFUOwwNcZGuWdP4EPgDUY96g9v5aXXNnhn-2BX8hItBHdA4zoFGTRRZIfkXYdNHYr0kFdZkQ7lwAxYztVkhdRsK7hWUdWlNgDTps6EI20&amp;source=gmail&amp;ust=1624861275724000&amp;usg=AFQjCNEp3x1fyNIaXjRigJupVfGihEvNFw"><img alt="Dyspatch Facebook" src="https://ci5.googleusercontent.com/proxy/KCPOsIHVv0XxeQRMCiqQAK5MLTEwl_Bw7rrybsG25r8rgpX2o-FNI2X1rc3puLKjBnD8b34YYcb8IZBvAq1_CejZm8FUyQ2X5NNn7IIlwYir62czRHJpbH9hur946Hs=s0-d-e1-ft#https://d1pgqke3goo8l6.cloudfront.net/BfKRGsdRB6s0fwhADpmA_icon-facebook.png" style="width:45px;margin:0px 5px;line-height:100%" class="CToWUd"> </a>
    <a href="http://fmtrack1.dyspatch.io/ls/click?upn=5EPtVKcEsZTOl0ymYbTSSnRyzHZQ5rH3ZhE2FmWG3myuF-2BVB4iDmsuemKrJMg-2BBHgBUTbpA9g6TpCQVjmmpRQFtX-2Fhqx9zsLEBSDK1l19gpWMCHpeNEzjwuT9LMRl1DvmpsCPqGOOdcdLLScpN-2BFMqZVUglIDyI7-2F7scW4-2BffHm8voYNksaO0SrG6amMB0OiSWlRNlIAB0dRlYZ6Hyels5PGOEZtbeKo90Lrbc0fop2nESvnANhckdgPIxFDQLP0IaqTWaO-2Fj6aCJL5Xv3MmBPiPZElAg72gioCOjSVwNq61y5ACEQ4CwfC3otqc3cnvH7bB_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU6cnT7jfWhbhOzl4Cd0UquucV-2FqC-2BFk1KPaDLVOmX-2Fr3Ds88ZXjAblFGbSXBRj0Kad0dXRuz-2FMYPYsEWrOtvI9v0r-2BOAaXrPuYgpLVT3s0ZnmbgM5KA9hqY1xcgANX9lVuczeAR0Sysf-2FDiXaPOqVHTP1YHwN7HMDh4ANT0Ik1U-2B" style="text-decoration:none;color:rgb(69,143,221)" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://fmtrack1.dyspatch.io/ls/click?upn%3D5EPtVKcEsZTOl0ymYbTSSnRyzHZQ5rH3ZhE2FmWG3myuF-2BVB4iDmsuemKrJMg-2BBHgBUTbpA9g6TpCQVjmmpRQFtX-2Fhqx9zsLEBSDK1l19gpWMCHpeNEzjwuT9LMRl1DvmpsCPqGOOdcdLLScpN-2BFMqZVUglIDyI7-2F7scW4-2BffHm8voYNksaO0SrG6amMB0OiSWlRNlIAB0dRlYZ6Hyels5PGOEZtbeKo90Lrbc0fop2nESvnANhckdgPIxFDQLP0IaqTWaO-2Fj6aCJL5Xv3MmBPiPZElAg72gioCOjSVwNq61y5ACEQ4CwfC3otqc3cnvH7bB_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU6cnT7jfWhbhOzl4Cd0UquucV-2FqC-2BFk1KPaDLVOmX-2Fr3Ds88ZXjAblFGbSXBRj0Kad0dXRuz-2FMYPYsEWrOtvI9v0r-2BOAaXrPuYgpLVT3s0ZnmbgM5KA9hqY1xcgANX9lVuczeAR0Sysf-2FDiXaPOqVHTP1YHwN7HMDh4ANT0Ik1U-2B&amp;source=gmail&amp;ust=1624861275724000&amp;usg=AFQjCNFdGAHW1cHGr3AplRG-3pHBm223xw"> <img alt="Dyspatch Twitter" src="https://ci6.googleusercontent.com/proxy/FFUaR7FNIM3iY_0ULM0Q1WniTkyrnh_iXU6d3HzlIV1JvnVIZiJ6JgwOraHrtBiPLnK-eiEFa3K4mtXZHTXh0i1ZqtsO0Tf8H-e2CZcDGjteDkh_EZNIJb6Y3mBYiQ=s0-d-e1-ft#https://d1pgqke3goo8l6.cloudfront.net/SMetMgVSFy0PiDiff5nz_icon-twitter.png" style="width:45px;margin:0px 5px;line-height:100%" class="CToWUd"> </a>
    <a href="http://fmtrack1.dyspatch.io/ls/click?upn=5EPtVKcEsZTOl0ymYbTSSkYBBZZhpOx5fsqi6S3NsUAHKDa0TZBQmONdKayfk8hDQtkY8rZ3y6mIG8ZfCFWe411sgcovnXSFqHv-2Bq5mAyBJDrjLmffYkxdge35GdGjyMk-2FL8R1vbCzOyhne6VWOjnxr7ipqP-2BrGU6jmUY-2Fevwylz-2FACgaK9lleZy-2BTF8LFwpQt48VDUMwGESPdxYs3hZxe9yU8HKYwvjdNiO83JPLlCONo9pci0ihvA9UAwgabG5-2FK1iQC1hdSUgqTshFzXAjxJYQx1A1pRZwTz0GH9cB0KFFEuR0Z-2F1fBaohldp6QZwepM6BnIUdVitPkdc8SCwag-3D-3D6QTC_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU0k1d1Sx-2BNAyuCq8B358eShf9Pg5C0jS4gtsP3AYcUCGSy3q893So5SSbwCVfUXeofXHt2dQ-2B-2BXn-2Bw4sN2G-2BL-2B6D52ApkeWSQoYS0LNVQBhfEzKZI-2FfpqxL14I0cv5yLADfcL-2FVNMt60a-2F-2BOP4j-2B7MoNRXzRE8N5bWEsfQJng6Io" style="text-decoration:none;color:rgb(69,143,221)" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://fmtrack1.dyspatch.io/ls/click?upn%3D5EPtVKcEsZTOl0ymYbTSSkYBBZZhpOx5fsqi6S3NsUAHKDa0TZBQmONdKayfk8hDQtkY8rZ3y6mIG8ZfCFWe411sgcovnXSFqHv-2Bq5mAyBJDrjLmffYkxdge35GdGjyMk-2FL8R1vbCzOyhne6VWOjnxr7ipqP-2BrGU6jmUY-2Fevwylz-2FACgaK9lleZy-2BTF8LFwpQt48VDUMwGESPdxYs3hZxe9yU8HKYwvjdNiO83JPLlCONo9pci0ihvA9UAwgabG5-2FK1iQC1hdSUgqTshFzXAjxJYQx1A1pRZwTz0GH9cB0KFFEuR0Z-2F1fBaohldp6QZwepM6BnIUdVitPkdc8SCwag-3D-3D6QTC_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU0k1d1Sx-2BNAyuCq8B358eShf9Pg5C0jS4gtsP3AYcUCGSy3q893So5SSbwCVfUXeofXHt2dQ-2B-2BXn-2Bw4sN2G-2BL-2B6D52ApkeWSQoYS0LNVQBhfEzKZI-2FfpqxL14I0cv5yLADfcL-2FVNMt60a-2F-2BOP4j-2B7MoNRXzRE8N5bWEsfQJng6Io&amp;source=gmail&amp;ust=1624861275724000&amp;usg=AFQjCNGyZt7bSd7l9zv-y7qkqB-OXLrZEw"> <img alt="Dyspatch Linkedin" src="https://ci4.googleusercontent.com/proxy/8zqnbVASTASF-2WnkVBpm7G0KaE1urnUZaSnRYJeyCGvtmBOJeZPfFDk6RMk5sx550IhYLlJA0GjVWXyeoA_XRpCg-gKJhXiWyb6-ciy0zNpN_MnjYjsWdnKW_pZ278=s0-d-e1-ft#https://d1pgqke3goo8l6.cloudfront.net/bH6gk5thTcWJYr0kMKGg_icon-linkedin.png" style="width:45px;margin:0px 5px;line-height:100%" class="CToWUd"> </a>
   </center>

   <div style="margin:0px auto;max-width:600px">
    <table align="center" border="0" cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse">
     <tbody>
      <tr>
       <td style="direction:ltr;font-size:0px;padding:20px 0px;text-align:center;vertical-align:top;border-collapse:collapse;border:0px">

        <div style="direction:ltr;display:inline-block;font-size:13px;text-align:left;vertical-align:top;width:100%">
         <table border="0" cellpadding="0" cellspacing="0" style="vertical-align:top;border-collapse:collapse" width="100%">
          <tbody>
           <tr>
            <td align="center" style="font-size:0px;padding:10px 25px;word-break:break-word;border-collapse:collapse;border:0px">
             <div style="color:#999999;font-family:Lato,Helvetica,Arial,sans-serif;font-size:12px;line-height:1.6;text-align:center">
              <span style="line-height:1"><a alt="Dyspatch home" href="http://fmtrack1.dyspatch.io/ls/click?upn=5EPtVKcEsZTOl0ymYbTSSt6bBmPavFQW770kxvG57IzokNVZMpTu4-2Frhwz9F-2BZC3c84S9qCuT-2Fhj-2FYlDHCmy-2BXT-2FmTzVsVfofJH-2F-2BFsjkJwrwocN73SAqKO4arWB81MFL-2Bszd4RG2IWtlDgVFDQJXpngJyKEBjdSk5ysVZKDF0mi8fpNujOxqvs5N82afLxIYap44ZZ-2FS8odHhSsPAEHk6FE7q5YblbcvaPDSQNr4iLyEljlfB84kFjNDpQoG1lhW6mNpxH2Pl0xutXyPwtvyxHLsusDR2UrfWtpP-2BodHhw-3DCkvo_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU2wqQacMNcp-2BgzVosl8XPZ2w1JKlg3yC-2BHPkijt1VLqFkDM78uLWuUlsicOsTbmetfXk2tJ0iyzzaesFnBff77D3ljS-2FBvCiJ5Ss8MvLUCWiBSIB35yyhuAoIbm4UlgzRYmAwfWdxkwLfJV8xqnQLP530dVR2l71-2FtAzQ0QahSPF" style="color:rgb(153,153,153);text-decoration:underline" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://fmtrack1.dyspatch.io/ls/click?upn%3D5EPtVKcEsZTOl0ymYbTSSt6bBmPavFQW770kxvG57IzokNVZMpTu4-2Frhwz9F-2BZC3c84S9qCuT-2Fhj-2FYlDHCmy-2BXT-2FmTzVsVfofJH-2F-2BFsjkJwrwocN73SAqKO4arWB81MFL-2Bszd4RG2IWtlDgVFDQJXpngJyKEBjdSk5ysVZKDF0mi8fpNujOxqvs5N82afLxIYap44ZZ-2FS8odHhSsPAEHk6FE7q5YblbcvaPDSQNr4iLyEljlfB84kFjNDpQoG1lhW6mNpxH2Pl0xutXyPwtvyxHLsusDR2UrfWtpP-2BodHhw-3DCkvo_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU2wqQacMNcp-2BgzVosl8XPZ2w1JKlg3yC-2BHPkijt1VLqFkDM78uLWuUlsicOsTbmetfXk2tJ0iyzzaesFnBff77D3ljS-2FBvCiJ5Ss8MvLUCWiBSIB35yyhuAoIbm4UlgzRYmAwfWdxkwLfJV8xqnQLP530dVR2l71-2FtAzQ0QahSPF&amp;source=gmail&amp;ust=1624861275725000&amp;usg=AFQjCNG76mKg0pWvUzr6gQv1c3NXLqGB7w">Website</a> | <a alt="Dyspatch blog" href="http://fmtrack1.dyspatch.io/ls/click?upn=5EPtVKcEsZTOl0ymYbTSSt6bBmPavFQW770kxvG57IwD7ilWC0Cu0bU4C0-2BEB6NSRWMAnKhAKMVYoLzG-2FVUcM7y79c2xBU-2FVB76-2FF5UhuN-2BgHaat6xc-2FeAcLCvkyLO-2BeH61abet-2BE2CgDs-2BVgUWY9qI-2BxhFeXnCC99LEsRIGPra1QcXdPTlXdAelXqFI-2FldcR2XweAsV4iHZNphRg568C91m-2FJC-2F01ayy2aYwjO6EqGhdRHDRBxEx1GsALvzTs1acsE33LrKB7P-2BYAv756OI-2FF0XIXXnE3DVt79nppz4KPEBj9JoHdQlJxpGPrl62ZhF5Qd-_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU4JtgKhjgre6a15ShF8pj-2BRmyXMSF23avqKSoZ59ccTPw2tXwliasjDRPSttDk6seXtrQ1F8B994Du0sI3LjRO7YYZMUNUueh-2F7V9ngMgQH6wRaiAiswydDcwlYFJCuezWVRtKHCAqHbUXmx03d60O55rYO3ZcYJt3fotzAW6vyp" style="color:rgb(153,153,153);text-decoration:underline" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://fmtrack1.dyspatch.io/ls/click?upn%3D5EPtVKcEsZTOl0ymYbTSSt6bBmPavFQW770kxvG57IwD7ilWC0Cu0bU4C0-2BEB6NSRWMAnKhAKMVYoLzG-2FVUcM7y79c2xBU-2FVB76-2FF5UhuN-2BgHaat6xc-2FeAcLCvkyLO-2BeH61abet-2BE2CgDs-2BVgUWY9qI-2BxhFeXnCC99LEsRIGPra1QcXdPTlXdAelXqFI-2FldcR2XweAsV4iHZNphRg568C91m-2FJC-2F01ayy2aYwjO6EqGhdRHDRBxEx1GsALvzTs1acsE33LrKB7P-2BYAv756OI-2FF0XIXXnE3DVt79nppz4KPEBj9JoHdQlJxpGPrl62ZhF5Qd-_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkU4JtgKhjgre6a15ShF8pj-2BRmyXMSF23avqKSoZ59ccTPw2tXwliasjDRPSttDk6seXtrQ1F8B994Du0sI3LjRO7YYZMUNUueh-2F7V9ngMgQH6wRaiAiswydDcwlYFJCuezWVRtKHCAqHbUXmx03d60O55rYO3ZcYJt3fotzAW6vyp&amp;source=gmail&amp;ust=1624861275725000&amp;usg=AFQjCNE5FfYuKtHdT2FVEfBveYYGhgmY6w">Blog</a> | <a alt="Dyspatch documentation" href="http://fmtrack1.dyspatch.io/ls/click?upn=5EPtVKcEsZTOl0ymYbTSSt6bBmPavFQW770kxvG57IwxWH-2BiyxEL0xBMkQn3eOUbcJ7nMtmgdmxWu5VPHrL13qTJ2PbKZNoh8EgHdj-2F7Ss3h1tAfi5mwEwkfRi0v1wlELDwgop8nJCZ9ByhtOUZWMHQPamV0P6chXxLUnstbW3TAm7J9PTi7WmzrR89r3KjN13xRZFGwjjaQNRDXU-2B3WWO2Po2VO9uD9R0RnpYhwOII3vUP3wGFfAp26voPJFzgOb54arX36rTXOGWAw-2BroWx-2BJ-2BZYhunShvcHDJh9-2BZ1xlJd3-2FjpU4PMxODeSuObqKbf-Yh_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkUxGaOVDmCfAFboT1jV40aHUsOf4lqUNXT3MciU3CITd4FsOi3Z6Q9idRaRcPxNY64Kz0KOrOiNjaTj8gKHUOP-2FSu7WiAp8emnFTWJr-2BsdOcUveA-2Fc-2FarBJvBnDZP5jpKHO6VWOI6zYi3co-2BGACn1ISsvmpR62G3lVDOjr-2F7JaMFT" style="color:rgb(153,153,153);text-decoration:underline" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://fmtrack1.dyspatch.io/ls/click?upn%3D5EPtVKcEsZTOl0ymYbTSSt6bBmPavFQW770kxvG57IwxWH-2BiyxEL0xBMkQn3eOUbcJ7nMtmgdmxWu5VPHrL13qTJ2PbKZNoh8EgHdj-2F7Ss3h1tAfi5mwEwkfRi0v1wlELDwgop8nJCZ9ByhtOUZWMHQPamV0P6chXxLUnstbW3TAm7J9PTi7WmzrR89r3KjN13xRZFGwjjaQNRDXU-2B3WWO2Po2VO9uD9R0RnpYhwOII3vUP3wGFfAp26voPJFzgOb54arX36rTXOGWAw-2BroWx-2BJ-2BZYhunShvcHDJh9-2BZ1xlJd3-2FjpU4PMxODeSuObqKbf-Yh_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkUxGaOVDmCfAFboT1jV40aHUsOf4lqUNXT3MciU3CITd4FsOi3Z6Q9idRaRcPxNY64Kz0KOrOiNjaTj8gKHUOP-2FSu7WiAp8emnFTWJr-2BsdOcUveA-2Fc-2FarBJvBnDZP5jpKHO6VWOI6zYi3co-2BGACn1ISsvmpR62G3lVDOjr-2F7JaMFT&amp;source=gmail&amp;ust=1624861275725000&amp;usg=AFQjCNGAPJ3HoU-Z-geA5eNjhf2n_p_XCA">Docs</a> | <a alt="Contact us" href="http://fmtrack1.dyspatch.io/ls/click?upn=5EPtVKcEsZTOl0ymYbTSSt6bBmPavFQW770kxvG57IzwWkI5KpkJ8kG7cDuc02IMSxYA0CCdvafkNynkmr0D5091cI3e8mPF-2FBIrrAYU4cIwaq6aZZZrpzcVNc8L8hd8MrZ6J0z4TMlMRj4rQ7y2epuPnN6FwenkoGnlOl3fOkZL-2FWuGv5VOv3iqp8euu-2FWNu9O9MLbi70DaQZ1BG3316mE1UP1OnaDaYx61hnEL26-2BtbCuh43kQNNzU9-2Ff8jVC-2B3WoMKyAZhjXD-2BUanwdDBOEpxpov7T3IeVcCCgwmR4-2Fqf7WpWYdF815QULNz2S8DIYP1g_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkUylaFuCZRPaVEZW-2FDuV9sJlv51uG1Z-2F6EJh-2BEA0PUXMrUO-2FZoJfN0mmyLSTduPrGc-2BBSZGyza3t-2FmybhzDxwMfvctEMxQDcYAjgTcxZRFYmMZzvIfcVgMotP5-2Fa1GDtMAGTxq9e-2Bf0v9w9yVwHEdSkwcU6pJQwgmutaa1xsF2-2BjL" style="color:rgb(153,153,153);text-decoration:underline" target="_blank" data-saferedirecturl="https://www.google.com/url?q=http://fmtrack1.dyspatch.io/ls/click?upn%3D5EPtVKcEsZTOl0ymYbTSSt6bBmPavFQW770kxvG57IzwWkI5KpkJ8kG7cDuc02IMSxYA0CCdvafkNynkmr0D5091cI3e8mPF-2FBIrrAYU4cIwaq6aZZZrpzcVNc8L8hd8MrZ6J0z4TMlMRj4rQ7y2epuPnN6FwenkoGnlOl3fOkZL-2FWuGv5VOv3iqp8euu-2FWNu9O9MLbi70DaQZ1BG3316mE1UP1OnaDaYx61hnEL26-2BtbCuh43kQNNzU9-2Ff8jVC-2B3WoMKyAZhjXD-2BUanwdDBOEpxpov7T3IeVcCCgwmR4-2Fqf7WpWYdF815QULNz2S8DIYP1g_ajJfDrlIJ-2FkdwAR41Gwy14rvzylVjBi2f16uLojTBd7cGm1MPkyA2BTrfjoMz0YAMvJsFCqf51k9Qly9vlMtBxlnsO2YvJrQ9eWqYHX4GH0Zuh7a6MvScbBnn6yHGTIV0nZk8uHaN6-2F9lIJ38VF0Fw9Ig7u47ZRz1UTqMNzPQNt2rlT0uBoFGN8ZOYdSirA4x3AYit7JfFn0vXfkgq-2FM0-2Bsxz5lbjAwLGh3Sxw3-2Fi8k0oJq-2F-2Fxa-2BN8OKVvMY3VrzDn0GXd-2FQEl64Tu-2B7y5drH7i9y0DT9hlUh4N1twq2oq0pCwlQhR-2BXDEVde4iia-2Fyx4dG26qXdVNA-2FQCKgvSL1GfUjBWVpkuH2T4hE7YuUbQyrcaVachOuHDMYykHFDYmhVBPhwqCUW44TVj4Nc8zz5tgFu4syA7mWB7FAGswuabXgFJYQk-2BF-2FPws7AIdBU4prPuzeJcNidFUsh1MjzigeD27uCE0-2B4r99sCMqGoWLi5LIRE5NLmdBcuY-2FjlpfyF5Y6xRb-2BRVQqRlhjOuXWBlVEHN-2FZhm7r77G4exHeHpNM3eu5XnZEhmIebCIFeqMqrnw4PCacQnRVCp12ntxirKtTUetVEfXUX7g1J6Ha1Awk1b6JdmsextSaTdb3q7xDb3nwQB2rjYROX-2BjLRt7OuJ5ptsz0hNLhOAM60DmnHsoEreD7BeI1JmTcZuu6C6ZFzNgSOQLo6CudZCmmzLzfnLsAATIPeGW0LEhIRLeOR2D1fY48wSM9dVjiur5npg5AYoMlNvE62KkJFhqxMBnhxZpVhz4VBxWFp8-2FDOy9XiRaCVLadh5aZzU9tPvP2jd7Gm5eZ2d3auy1PxbMldWMMIUkUylaFuCZRPaVEZW-2FDuV9sJlv51uG1Z-2F6EJh-2BEA0PUXMrUO-2FZoJfN0mmyLSTduPrGc-2BBSZGyza3t-2FmybhzDxwMfvctEMxQDcYAjgTcxZRFYmMZzvIfcVgMotP5-2Fa1GDtMAGTxq9e-2Bf0v9w9yVwHEdSkwcU6pJQwgmutaa1xsF2-2BjL&amp;source=gmail&amp;ust=1624861275725000&amp;usg=AFQjCNHSOvpWtEpxRN83Iua6iUEc6fY3BQ">Contact Us</a></span>
              <br>
              <br> Dyspatch, 747 Fort St, Victoria BC, Canada
              <br>
              <br>
              <span style="line-height:1">© 2021&nbsp;All Rights Reserved.<br> <br> <br> <br> <a href="https://sendwithus.myfreshworks.com/crm/marketer/mas/api/v1/subscription-preferences?fm_digest=93AAF2D51CB4ACCFDF5D05BA454FC0C9D1EAE269E756B0DB771CD8348DC99E37C5681E717B4AB46E13FD30A68426DA6EB27A69A55D77C2804B1408B0FBCC383B383DA6F5E18B38FE1C40FA70D7023934C9CDEC272AB72F457B6F38452836FE5D526EE64D26BF9A9B3C3E38D7241D6E14728C6D9484BAEAE4DADBEE8C32E45F41B4C0DB627D04675671E7E505203E6B05A30B5F8C17A1B2D3E2D8E7C9B9F7365E1A097120ECFAB89AE3E800CE469831966780206F5B02D59F78C273019C60E6661214A8F33B3462E74CD4FD740B6034F00B100D1B6C1FABF0BC6088FF61CAB4756990C2A3197969B2B414AE060FF36D0A5ADC84A96899A998B691243D7579F5DA" style="color:rgb(69,143,221);text-decoration:underline" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://sendwithus.myfreshworks.com/crm/marketer/mas/api/v1/subscription-preferences?fm_digest%3D93AAF2D51CB4ACCFDF5D05BA454FC0C9D1EAE269E756B0DB771CD8348DC99E37C5681E717B4AB46E13FD30A68426DA6EB27A69A55D77C2804B1408B0FBCC383B383DA6F5E18B38FE1C40FA70D7023934C9CDEC272AB72F457B6F38452836FE5D526EE64D26BF9A9B3C3E38D7241D6E14728C6D9484BAEAE4DADBEE8C32E45F41B4C0DB627D04675671E7E505203E6B05A30B5F8C17A1B2D3E2D8E7C9B9F7365E1A097120ECFAB89AE3E800CE469831966780206F5B02D59F78C273019C60E6661214A8F33B3462E74CD4FD740B6034F00B100D1B6C1FABF0BC6088FF61CAB4756990C2A3197969B2B414AE060FF36D0A5ADC84A96899A998B691243D7579F5DA&amp;source=gmail&amp;ust=1624861275725000&amp;usg=AFQjCNEPmnf8Bl1gKuah3BCOoi1XZO0MRQ"><span style="color:rgb(102,102,102)">Unsubscribe</span></a></span>
             </div></td>
           </tr>
          </tbody>
         </table>
        </div></td>
      </tr>
     </tbody>
    </table>
   </div>

  </div>'''


def send_reset_password_email(token):
    return f'''
    Hi Kindly click on the <a href="https://uniqueaccent.com.ng/accounts/resetPassword/{token}">link</a> 
    to reset your password.
    
    <a href="https://uniqueaccent.com.ng/accounts/resetPassword/{token}">{token}</a> 
    '''


def password_reset_confirmation(user_account):
    return f'''
    Hi {user_account.name} This is to confirm that your password had been reset successfully.
    '''


def send_email(subject, message, recipient_list, text_message=''):
    try:
        send_mail(
            subject=subject,
            html_message=message,
            recipient_list=recipient_list,
            message=text_message if text_message != '' else message,
            from_email='austineforall@gmail.com',
        )
        return True
    except:
        return False

