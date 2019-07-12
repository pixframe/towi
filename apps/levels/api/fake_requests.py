req = {
    "header": {
        "date": "2018-06-20 13:00:00",
        "parentid": 2,
        "cid": 7,
        "gameKey": "PruebaEcologica",
        "gameTime": 10,
        "passedLevels": 3,
        "repeatedLevels": 1,
        "playedLevels": 3,
        "version": "texto",
        "device": "texto"
    },
    "levels": {
        "boarding_latency": 10.2,
        "boarding_age": 2,
        "boarding_birthday": "texto",
        "boarding_time1": 1,
        "boarding_name": "texto",
        "boarding_address": "texto",
        "boarding_currentdate": "texto",
        "boarding_time2": 2,
        "packforward_tutorial": 2,
        "packforward_time": 1.10,
        "packforward_incorrect_secuence": 2,
        "packforward_instrusions": 2,
        "packbackward_tutorial": 2,
        "packforward_score": 2,
        "packbackward_score": 2,
        "packbackward_time": 2.2,
        "packbackward_incorrect_secuence": 2,
        "packbackward_intrusions": 2,
        "weather_latency": 2.2 ,
        "weather_object_packed": "texto",
        "weather_time": 2.2,
        "lab_start_level": 1,
        "lab1_time": 1.2,
        "lab2_time": 1.2 ,
        "lab3_time": 1.2 ,
        "lab1_latency": 1.2,
        "lab2_latency": 1.2,
        "lab3_latency": 1.2,
        "lab1_hits": 2,
        "lab2_hits": 2,
        "lab3_hits": 2,
        "lab1_crosses": 2,
        "lab2_crosses": 2,
        "lab3_crosses": 2,
        "lab1_deadends": 2,
        "lab2_deadends": 2,
        "lab3_deadends": 2,
        "lab1_changeofroutes": 1,
        "lab2_changeofroutes": 1,
        "lab3_changeofroutes": 1,
        "lab_mhits": 2.2,
        "lab_mcrosses": 2.2,
        "lab_mdeadends": 2.2,
        "lab_time": 10,
        "waitroom_correct": 1,
        "waitroom_incorrect": 1,
        "waitroom_correct_mlatency": 2.2,
        "waitroom_incorrect_mlatency": 2.2,
        "waitroom_tutorial": 2,
        "flyplane_tutorial": 2,
        "flyplane_series": 2,
        "flyplane_correct": 2,
        "flyplane_incorrect": 2,
        "flyplane_missed": 2,
        "flyplane_greencorrect": 2,
        "flyplane_greenincorrect": 2,
        "flyplane_greenmissed": 2,
        "flyplane_time": 2,
        "coins_tutorial": 2,
        "coins_level": 2,
        "coins_min_correct": 2,
        "coins_min_incorrect": 2,
        "coins_extra_correct": 2,
        "coins_extra_incorrect": 2,
        "coins_extra_missed": 2,
        "coins_correct_mlatency": 2.2,
        "coins_incorrect_mlatency": 2.2,
        "coins_selected": "texto",
        "coins_organization_score": 3,
        "coins_clickfinish_before_min": 3,
        "coins_time": 3,
        "unpack_correct": 3,
        "unpack_incorrect": 3,
        "unpack_perseveration": 3,
        "unpack_first_selected": "texto",
        "unpack_first_correct": "texto",
        "unpack_bad_recognition": 4,
        "unpack_time": 3.3,
        "arrange_amplitude": 2,
        "arrange1_correct": 2,
        "arrange2_correct": 2,
        "arrange3_correct": 2,
        "arrange1_incorrect": 2,
        "arrange2_incorrect": 2,
        "arrange3_incorrect": 2,
        "arrange1_perseveration": 2,
        "arrange2_perseveration": 2,
        "arrange3_perseveration": 2,
        "arrange_learningcurve": 2,
        "arrange_primacy": "texto",
        "arrange_recence": "texto",
        "arrange_spacialprecision_score": 3,
        "arrange_spacialprecision_sample": "texto",
        "arrange_storage_efficency1": 2,
        "arrange_storage_efficency2": 2,
        "arrange_incorrect_repeated": "texto",
        "arrange_correct_mlatency": 2.2,
        "arrange_incorrect_mlatency": 2.2,
        "arrange_time": 2,
        "arrange_perc_correct": 2.2,
        "total_time": 2.2
    }
}

am_req = {
    "header": {
        "date": "2018-06-20 13:00:00",
        "parentid": 1,
        "cid": 1,
        "gameKey": "ArbolMusical",
        "gameTime": 10,
        "passedLevels": 3,
        "repeatedLevels": 1,
        "playedLevels": 3
    },
    "levels": [
        {
            "birds": 2,
            "nests": 3,
            "level": 3,
            "sublevel": 2,
            "tutorial": 1,
            "sound": "sonidito",
            "birdSound": "sonidito 2",
            "time": 140,
            "birdListenedPre": "si",
            "birdListened": "no",
            "errors": 0,
            "correct": 10
        }
    ]
}

arenam_req = {
    "header": {
        "date": "2018-06-20 13:00:00",
        "parentid": 1,
        "cid": 1,
        "gameKey": "ArenaMagica",
        "gameTime": 10,
        "passedLevels": 3,
        "repeatedLevels": 1,
        "playedLevels": 3
    },
    "levels": [
        {
            "levelKey": "ArenaMagica",
            "level": 3,
            "subLevel": 2,
            "time": 1,
            "passed": 2,
            "repeated": 1,
            "accuracy": 140
        }
    ]
}


register_parent_child_req = {
    "parent_email": "buoc@towi.com.mx",
    "parent_password": "prueba",
    "child_name": "Regina",
    "child_dob": "2012-12-12"
}


update_profile = {
    "cid": 1,
    "kiwis": 10,
    "avatar": "towi",
    "avatarclothes": "vestido",
    "owneditems": "todos",
    "activemissions": [
        "Rio",
        "Tesoro"
    ],
    "activeday": 299,
    "rioFirstTime": true,
    "tesoroFirstTime": true,
    "arbolFirstTime": true,
    "arenaFirstTime": true,
    "sombrasFirstTime": true,
    "bolitaFirstTime": false,
    "userKey": "325a7123e0b9e4a7fe6473e243fb76d3ccf230db2704d9f88e89bc25476345c0"
}


{
    'parent_id': 2,
    "child_name": "Regina",
    "child_dob": "2012-12-12"
}
