for i in range(1, 19):
    print('<div class="mySlides fade">')
    print(f'\t<div class="numbertext">{i} / 18</div>')
    print(f'\t<img src=".\graphs\\activity\\{str(i).zfill(2)}.01.png" style="width:100%">')
    print('</div>')

# <div class="mySlides fade">
#     <div class="numbertext">1 / 3</div>
#     <img src="https://picsum.photos/500/250" style="width:100%">
#     <!-- <div class="text">Caption Text</div> -->
# </div>