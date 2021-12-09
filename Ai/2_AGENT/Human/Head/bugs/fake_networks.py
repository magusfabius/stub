/**
 * Instagram web unfollow script
 *
 * WHAT IS IT?
 * A script to unfollow people in the instagram website
 *
 * WHY?
 * I needed to clean my account so I quickly did this
 *
 * HOW TO USE:
 * Go to your instagram profile while logged in and run the following code in your console
 *
 * WHAT DOES IT DO EXACTLY?
 * It opens your followers list and goes one by one unfollowing with a random interval of 1 to 10
 * seconds in between
 *
 * CAN I GET BANNED?
 * Yes, although you will first be notified several times about strange activity
 * Simply put, use it at your own risk and not for long.
 *
 * Created on 15/03/17.
 * @author Joel Hernandez <involvmnt@gmail.com>
 */

openFollowersWindow().then(function () {
    populateUnfollowsPool();
    digestUnfollowsPool();
});

function openFollowersWindow() {
    var onFollowersWindowWasOpenedListeners = [];
    var openWindowTimeout = 3000;

    var followersElement = getFollowersElement();
    followersElement.click();

    function digestOnFollowersWindowWasOpenedListeners() {
        onFollowersWindowWasOpenedListeners.forEach(function (onFollowersWindowWasOpenedListener) {
            onFollowersWindowWasOpenedListener();
        });
    }

    var wasOpened;
    setTimeout(function () {
        // TODO Verify that the window was indeed opened
        wasOpened = true;
        digestOnFollowersWindowWasOpenedListeners();
    }, openWindowTimeout);
    return {
        then: function (onFollowersWindowWasOpened) {
            if (wasOpened) {
                onFollowersWindowWasOpened();
            } else {
                onFollowersWindowWasOpenedListeners.push(onFollowersWindowWasOpened);
            }
        }
    };
}

function getFollowersElement() {
    return getFollowersElementWithUsername(getUsername());
}

function getUsername() {
    var pageTitleElement = document.getElementsByTagName('h1')[0];
    if (!pageTitleElement) throw new Error('No title to get username from');
    return pageTitleElement.innerHTML;
}

function getFollowersElementWithUsername(username) {
    var followersElement = document.querySelectorAll('a[href="/' + username + '/following/"]')[0];
    if (!followersElement) throw new Error('No followers element was found');
    return followersElement;
}

var unfollowsPool;

function populateUnfollowsPool() {
    var buttons = document.getElementsByTagName('button');
    unfollowsPool = [];
    for (var i = 0; i < buttons.length; i++) {
        var button = buttons[i];
        if (button.innerHTML.includes('Following')) {
            var randomTimeoutForUnfollow = Math.floor((Math.random() * 10) + 1) * 1000;
            console.log('Following button!');

            var unfollow = {
                buttonElement: button,
                timeout: randomTimeoutForUnfollow
            };

            unfollowsPool.push(unfollow);
        }
    }
}

function digestUnfollowsPool() {
    if (unfollowsPool.length === 0) {
        console.log('Unfollow pool empty, repopulating');
        populateUnfollowsPool();
    }
    var unfollow = unfollowsPool.shift();
    var unfollowTimeout = unfollow.timeout;
    console.log('Clicking unfollow button in ', unfollowTimeout);
    setTimeout(function () {
        var unfollowButtonElement = unfollow.buttonElement;
        unfollowButtonElement.scrollIntoView(true);
        console.log('Clicking unfollow button');
        unfollowButtonElement.click();
        console.log('Clicked. Continuing digesting unfollow pool');
        digestUnfollowsPool();
    }, unfollowTimeout);
}