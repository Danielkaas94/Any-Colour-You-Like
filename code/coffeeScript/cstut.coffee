

# https://www.youtube.com/watch?v=LwYGPc-6sa0 - 7:45

###
    Multi
    line
    comment
###


name = "Uncle phil"

csOutput = document.getElementById("csoutput")

csOutput.innerHTML = "Hellow #{name}<br>"

aString = "Jeg er en string"

csOutput.insertAdjacentHTML('beforeend',
    'aString is a String<br>') if typeof aString is 'string'


largestNum = Number.MAX_VALUE
smallestNum = Number.MIN_VALUE

largeNumStr = "The largest number is #{largestNum}"
smallNumStr = "The smallest number is #{smallestNum}"

csOutput.insertAdjacentHTML('beforeend',
    largeNumStr + '<br>')

csOutput.insertAdjacentHTML('beforeend',
    smallNumStr + '<br>')


areYouHappy = yes
areYouOnFire = no

csOutput.insertAdjacentHTML('beforeend',
    'areYouHappy is a Boolean<br>') if typeof areYouHappy is 'boolean'