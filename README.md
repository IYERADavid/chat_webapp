                                                                # chat_webapp
                                                                
                                                           basic structure of this rep
                                            -----------------------------------------------------


chat web app:
    @ client side:
        - pages:
            * index
                { it is for welcom to our clients }
            * home
                { it shows basic interface for our clients and also search}
            * about
                { it show what service we provide}
            * contact
                { it shows our address }
            * profile
                { it shows profile picture,followers,following,owners biography,etc }
            * notifications
                { it shows who have followed you,who you can follow(suggestions) ,
                  what is your follow have done }
            * chat & group(messages)
                { your messages and also active people }
            * photo&video
                { her you can upload a video and a photo and some descriptions }
            * status
                { it can be video or photo and it is for 24hrs only }
            * menu(settings)
                { this a menu panel for dark mode ,etc }
        - database table:
            # table: user
                table-data:
                    * first-name
                    * middlename
                    * last name
                    * email / phone
                    * password
                    * total-followers
                    * total-following
                    * active
                    * creation-time
            # table: profile
                table-data:
                    * primary-id
                    * user-id
                    * picture
                    * current(it show which picture is shown as your profile)
                    * active
                    * time keeped
            # table: status
                table-data:
                    * primary-id
                    * user-id
                    * photo/video/text
                    * active
                    * time keeped
            # table: media
                table-data:
                    * primary-id
                    * user-id
                    * photos/videos/quotes/audio
                    * active
                    * time keeped
            # table: group
                table-data:
                    * primary-id
                    * founder-id
                    * group-name
                    * group-members
                    * time keeped
            # table: chat
              // must be in your followers
                table-data:
                    * primary-id
                    * sender-id
                    * message/photo/video/audio/files
                    * receiver-id / group
                    * active
                    * seen (yes/no)
                    * time keeped
            # table: follow
                table-data:
                    * primary-id
                    * following-id
                    * follower-id
                    * active
                    * time keeped
            # table: notification
                table-data:
                    * primary-id
                    * owner-id(user-id)
                    * message
                    * seen (yes/no)
                    * active
                    * time keeped
        # todo distinguish public and private accounts
    @ admin-side:
        -pages:
            * home
                { basic interface for admin }
            * account-details
                { both deleted data and active ones }
            * top-account
                { check by many folowers }
            * sending global-notification
                { notification for all users }

        END
