# THIRD PARTY IMPORTS
from import_export import resources
from import_export.fields import Field

# TOWI IMPORTS
from .models import (
    ChildrenTowiIsland, ArbolMusicalV2, ArenaMagicaV2,
    DondeQuedoLaBolitaV2, RecoleccionTesoroV2, RioV2, SombrasV2,
    Quartile, Average, Prueba
)
from .helpers import changue_grade_to_english, changue_laterality_to_english, changue_genre_to_english


class HeaderFullResource(resources.Resource):
    parent_email = Field(attribute='header__cid__user__email', column_name='admin_email')
    parent_firstname = Field(attribute='header__cid__user__first_name', column_name='admin_name')
    parent_lastname = Field(attribute='header__cid__user__last_name', column_name='admin_lastname')
    parent_country = Field(attribute='header__cid__user__country', column_name='admin_country')
    cid_id = Field(attribute='header__cid__id', column_name='child_id')
    cid_firstname = Field(attribute='header__cid__first_name', column_name='child_name')
    cid_lastname = Field(attribute='header__cid__last_name', column_name='child_lastname')
    cid_dob = Field(attribute='header__cid__dob', column_name='child_birthdate')
    cid_grade = Field(attribute='header__cid__grade', column_name='child_grade')
    cid_genre = Field(attribute='header__cid__genre', column_name='child_sex')
    cid_laterality = Field(attribute='header__cid__laterality', column_name='child_laterality')
    cid_videogames_usage = Field(attribute='header__cid__videogames_usage', column_name='child_videogames_usage')
    cid_diagnostic = Field(attribute='header__cid__diagnostic', column_name='child_learning_disabilities')
    cid_failed_grades = Field(attribute='header__cid__failed_grades', column_name='child_failed_grades')
    cid_school_name = Field(attribute='header__cid__school__name', column_name='school_name')
    cid_school_type = Field(attribute='header__cid__school__type', column_name='school_public_private')
    cid_school_city = Field(attribute='header__cid__school__city', column_name='school_city')
    cid_school_regular_special = Field(attribute='header__cid__school__regular_special', column_name='school_regular_special')
    cid_school_mixed_differetiated = Field(attribute='header__cid__school__mixed_differetiated', column_name='school_mixed_differentiated')
    header_version = Field(attribute='header__version', column_name='assessment_version')
    header_date = Field(attribute='header__date', column_name='assessment_date')
    header_device = Field(attribute='header__device', column_name='assessment_device')
    header_application_number = Field(attribute='application_number', column_name='assessment_application_number')

    class Meta:
        export_order = (
            'parent_email',
            'parent_firstname',
            'parent_lastname',
            'parent_country',
            'cid_id',
            'cid_firstname',
            'cid_lastname',
            'cid_dob',
            'cid_grade',
            'cid_genre',
            'cid_laterality',
            'cid_videogames_usage',
            'cid_diagnostic',
            'cid_failed_grades',
            'cid_school_name',
            'cid_school_type',
            'cid_school_regular_special',
            'cid_school_mixed_differetiated',
            'cid_school_city',
            'header_version',
            'header_date',
            'header_device',
            'header_application_number',     
        )


class HeaderLimitedResource(resources.Resource):
    parent_country = Field(attribute='header__cid__user__country', column_name='admin_country')
    cid_id = Field(attribute='header__cid__id', column_name='child_id')
    cid_dob = Field(attribute='header__cid__dob', column_name='child_birthdate')
    cid_grade = Field(attribute='header__cid__grade', column_name='child_grade')
    cid_genre = Field(attribute='header__cid__genre', column_name='child_sex')
    cid_laterality = Field(attribute='header__cid__laterality', column_name='child_laterality')
    cid_videogames_usage = Field(attribute='header__cid__videogames_usage', column_name='child_videogames_usage')
    cid_diagnostic = Field(attribute='header__cid__diagnostic', column_name='child_learning_disabilities')
    cid_failed_grades = Field(attribute='header__cid__failed_grades', column_name='child_failed_grades')
    cid_school_type = Field(attribute='header__cid__school__type', column_name='school_public_private')
    cid_school_city = Field(attribute='header__cid__school__city', column_name='school_city')
    cid_school_regular_special = Field(attribute='header__cid__school__regular_special', column_name='school_regular_special')
    cid_school_mixed_differetiated = Field(attribute='header__cid__school__mixed_differetiated', column_name='school_mixed_differentiated')
    header_version = Field(attribute='header__version', column_name='assessment_version')
    header_date = Field(attribute='header__date', column_name='assessment_date')
    header_device = Field(attribute='header__device', column_name='assessment_device')
    header_application_number = Field(attribute='application_number', column_name='assessment_application_number')

    class Meta:
        export_order = (
            'parent_country',
            'cid_id',
            'cid_dob',
            'cid_grade',
            'cid_genre',
            'cid_laterality',
            'cid_videogames_usage',
            'cid_diagnostic',
            'cid_failed_grades',
            'cid_school_type',
            'cid_school_mixed_differetiated',
            'cid_school_regular_special',
            'cid_school_city',
            'header_version',
            'header_date',
            'header_device',
            'header_application_number',
        )


class FormatNumberPruebaResource(resources.Resource):
    id = Field(attribute='id', column_name='assessment_id')
    arrange_recence = Field(attribute='arrange_recence', column_name='arrange_recency')
    arrange_spacialprecision_score = Field(attribute='arrange_spacialprecision_score', column_name='arrange_spatialprecision_score')
    arrange_spacialprecision_sample = Field(attribute='arrange_spacialprecision_sample', column_name='arrange_spatialprecision_sample')
    weather_object_packed = Field(attribute='weather_object_packed', column_name='weather_packed_objects')

    class Meta:
        model = Prueba

    def dehydrate_lab1_time(self, prueba):
        return format(prueba.lab1_time, '.4f')
    
    def dehydrate_lab2_time(self, prueba):
        return format(prueba.lab2_time, '.4f')
    
    def dehydrate_lab3_time(self, prueba):
        return format(prueba.lab3_time, '.4f')
    
    def dehydrate_lab1_latency(self, prueba):
        return format(prueba.lab1_latency, '.4f')
        
    def dehydrate_lab2_latency(self, prueba):
        return format(prueba.lab2_latency, '.4f')
    
    def dehydrate_lab3_latency(self, prueba):
        return format(prueba.lab3_latency, '.4f')
    
    def dehydrate_boarding_time1(self, prueba):
        return format(prueba.boarding_time1, '.4f')
    
    def dehydrate_boarding_time2(self, prueba):
        return format(prueba.boarding_time2, '.4f')
    
    def dehydrate_weather_latency(self, prueba):
        if prueba.weather_latency is None:
            return ' '
        else:
            return format(prueba.weather_latency, '.4f')

    def dehydrate_weather_time(self, prueba):
        if prueba.weather_time is None:
            return ' '
        else:
            return format(prueba.weather_time, '.4f')

    def dehydrate_packforward_time(self, prueba):
        if prueba.packforward_time is None:
            return ' '
        else:
            return format(prueba.packforward_time, '.4f')

    def dehydrate_packbackward_time(self, prueba):
        if prueba.packbackward_time is None:
            return ' '
        else:
            return format(prueba.packbackward_time, '.4f')

    def dehydrate_arrange_perc_correct(self, prueba):
        return '{} %'.format(prueba.arrange_perc_correct)
    
    def dehydrate_arrange_primacy(self, prueba):
        va = prueba.arrange_primacy
        for value in va:
            if value.find('['):
                return '{}'.format(prueba.arrange_primacy[:7])
            return ' '

    def dehydrate_arrange_recence(self, prueba):
        va = prueba.arrange_recence
        for value in va:
            if value.find('['):
                return '{}'.format(prueba.arrange_recence[:7])
            return ' '
    
    def dehydrate_weather_object_packed(self, prueba):
        wop = prueba.weather_object_packed
        for value in wop:
            if value.find('-'):
                return prueba.weather_object_packed
            return ' '

    def dehydrate_parent_country(self, prueba):
        country = prueba.header.cid.user.country
        for value in country:
            if value.find('MX'):
                return '3996063|Mexico'
            return ' '

    def dehydrate_cid_laterality(self, prueba):
        value = prueba.header.cid.laterality
        laterality = changue_laterality_to_english(value)
        return laterality
    
    def dehydrate_cid_genre(self, prueba):
        value = prueba.header.cid.genre
        genre = changue_genre_to_english(value)
        return genre

    def dehydrate_cid_grade(self, prueba):
        value = prueba.header.cid.grade
        grade = changue_grade_to_english(value)
        return grade


class PruebasFullResource(resources.ModelResource, HeaderFullResource, FormatNumberPruebaResource):

    class Meta:
        model = Prueba
        export_order = (
            'parent_email',
            'parent_firstname',
            'parent_lastname',
            'parent_country',
            'cid_id',
            'cid_firstname',
            'cid_lastname',
            'cid_dob',
            'cid_grade',
            'cid_genre',
            'cid_laterality',
            'cid_videogames_usage',
            'cid_diagnostic',
            'cid_failed_grades',
            'cid_school_name',
            'cid_school_type',
            'cid_school_mixed_differetiated',
            'cid_school_regular_special',
            'cid_school_city',
            'header_version',
            'header_date',
            'header_device',
            'header_application_number',
            'id',
            'boarding_latency',            
            'boarding_age',
            'boarding_birthday',
            'boarding_time1',
            'boarding_name',
            'boarding_address',
            'boarding_currentdate',
            'boarding_time2',
            'packforward_tutorial',
            'packforward_time',
            'packforward_incorrect_secuence',
            'packforward_instrusions',
            'packbackward_tutorial',
            'packforward_score',
            'packbackward_score',
            'packbackward_time',
            'packbackward_incorrect_secuence',
            'packbackward_intrusions',
            'weather_latency',
            'weather_object_packed',
            'weather_time',
            'lab_start_level',
            'lab1_time',
            'lab2_time',
            'lab3_time',
            'lab1_latency',	
            'lab2_latency',
            'lab3_latency',
            'lab1_hits',
            'lab2_hits',
            'lab3_hits',
            'lab1_crosses',	
            'lab2_crosses',
            'lab3_crosses',
            'lab1_deadends',	
            'lab2_deadends',
            'lab3_deadends',
            'lab1_changeofroutes',
            'lab2_changeofroutes',	
            'lab3_changeofroutes',	
            'lab_mhits',
            'lab_mcrosses',
            'lab_mdeadends',
            'lab_time',
            'waitroom_tutorial',
            'waitroom_correct',
            'waitroom_incorrect',
            'waitroom_correct_mlatency',
            'waitroom_incorrect_mlatency',	
            'flyplane_series',
            'flyplane_tutorial',
            'flyplane_correct',
            'flyplane_incorrect',
            'flyplane_missed',
            'flyplane_greencorrect',
            'flyplane_greenincorrect',	
            'flyplane_greenmissed',
            'flyplane_time',
            'flyplane_correct_mlatency',
            'flyplane_incorrect_mlatency',	
            'flyplane_greencorrect_mlatency',
            'flyplane_greenincorrect_mlatency',	
            'coins_level',
            'coins_min_correct',
            'coins_min_incorrect',	
            'coins_extra_correct',	
            'coins_extra_incorrect',	
            'coins_extra_missed',
            'coins_selected',
            'coins_organization_score',
            'coins_clickfinish_before_min',
            'coins_time',
            'unpack_correct',
            'unpack_incorrect',	
            'unpack_perseveration',
            'unpack_first_selected',	
            'unpack_first_correct',
            'unpack_bad_recognition',	
            'unpack_time',
            'arrange_amplitude',
            'arrange1_correct',
            'arrange2_correct',
            'arrange3_correct',
            'arrange1_incorrect',	
            'arrange2_incorrect',
            'arrange3_incorrect',
            'arrange1_perseveration',
            'arrange2_perseveration',
            'arrange3_perseveration',
            'arrange_learningcurve',
            'arrange_primacy',
            'arrange_recence',
            'arrange_spacialprecision_score',
            'arrange_spacialprecision_sample',
            'arrange_storage_efficency1',
            'arrange_storage_efficency2',
            'arrange_incorrect_repeated',
            'arrange_time',
            'arrange_perc_correct',
            'total_time',
        )
        exclude = (
            'header',
            'coins_tutorial',
            'coins_correct_mlatency',
            'coins_incorrect_mlatency',
            'coins_pattern_type',
            'arrange_correct_mlatency',
            'arrange_incorrect_mlatency',   
        )


class PruebasDefaultResource(resources.ModelResource, HeaderLimitedResource, FormatNumberPruebaResource):

    class Meta:
        model = Prueba
        export_order = (
            'parent_country',
            'cid_id',
            'cid_dob',
            'cid_grade',
            'cid_genre',
            'cid_laterality',
            'cid_videogames_usage',
            'cid_diagnostic',
            'cid_failed_grades',
            'cid_school_type',
            'cid_school_mixed_differetiated',
            'cid_school_regular_special',
            'cid_school_city',
            'header_version',
            'header_date',
            'header_device',
            'header_application_number',
            'id',
            'boarding_latency',
            'boarding_age',
            'boarding_birthday',
            'boarding_time1',
            'boarding_currentdate',
            'boarding_time2',
            'packforward_tutorial',
            'packforward_time',
            'packforward_incorrect_secuence',
            'packforward_instrusions',
            'packbackward_tutorial',
            'packforward_score',
            'packbackward_score',
            'packbackward_time',
            'packbackward_incorrect_secuence',
            'packbackward_intrusions',
            'weather_latency',
            'weather_object_packed',
            'weather_time',
            'lab_start_level',
            'lab1_time',
            'lab2_time',
            'lab3_time',
            'lab1_latency',	
            'lab2_latency',
            'lab3_latency',
            'lab1_hits',
            'lab2_hits',
            'lab3_hits',
            'lab1_crosses',	
            'lab2_crosses',
            'lab3_crosses',
            'lab1_deadends',	
            'lab2_deadends',
            'lab3_deadends',
            'lab1_changeofroutes',
            'lab2_changeofroutes',	
            'lab3_changeofroutes',	
            'lab_mhits',
            'lab_mcrosses',
            'lab_mdeadends',
            'lab_time',
            'waitroom_tutorial',
            'waitroom_correct',
            'waitroom_incorrect',
            'waitroom_correct_mlatency',
            'waitroom_incorrect_mlatency',
            'flyplane_series',
            'flyplane_tutorial',
            'flyplane_correct',
            'flyplane_incorrect',
            'flyplane_missed',
            'flyplane_greencorrect',
            'flyplane_greenincorrect',	
            'flyplane_greenmissed',
            'flyplane_time',
            'flyplane_correct_mlatency',
            'flyplane_incorrect_mlatency',	
            'flyplane_greencorrect_mlatency',
            'flyplane_greenincorrect_mlatency',	
            'coins_level',
            'coins_min_correct',
            'coins_min_incorrect',	
            'coins_extra_correct',	
            'coins_extra_incorrect',	
            'coins_extra_missed',
            'coins_selected',
            'coins_organization_score',
            'coins_clickfinish_before_min',
            'coins_time',
            'unpack_correct',
            'unpack_incorrect',	
            'unpack_perseveration',
            'unpack_first_selected',	
            'unpack_first_correct',
            'unpack_bad_recognition',	
            'unpack_time',
            'arrange_amplitude',
            'arrange1_correct',
            'arrange2_correct',
            'arrange3_correct',
            'arrange1_incorrect',	
            'arrange2_incorrect',
            'arrange3_incorrect',
            'arrange1_perseveration',
            'arrange2_perseveration',
            'arrange3_perseveration',
            'arrange_learningcurve',
            'arrange_primacy',
            'arrange_recence',
            'arrange_spacialprecision_score',
            'arrange_spacialprecision_sample',
            'arrange_storage_efficency1',
            'arrange_storage_efficency2',
            'arrange_incorrect_repeated',
            'arrange_time',
            'arrange_perc_correct',
            'total_time',
        )
        exclude = (
            'playername',
            'playeraddress',
            'playerage',
            'playerbirthday',
            'boarding_address',
            'boarding_name',
            'header',
            'coins_tutorial',
            'coins_correct_mlatency',
            'coins_incorrect_mlatency',
            'coins_pattern_type',
            'arrange_correct_mlatency',
            'arrange_incorrect_mlatency',
        )


class HeaderGamesFullResource(resources.Resource):
    parent_email = Field(attribute='header__cid__user__email', column_name='admin_email')
    parent_firstname = Field(attribute='header__cid__user__first_name', column_name='admin_name')
    parent_lastname = Field(attribute='header__cid__user__last_name', column_name='admin_lastname')
    parent_country = Field(attribute='header__cid__user__country', column_name='admin_country')
    cid_id = Field(attribute='header__cid__id', column_name='child_id')
    cid_firstname = Field(attribute='header__cid__first_name', column_name='child_name')
    cid_lastname = Field(attribute='header__cid__last_name', column_name='child_lastname')
    cid_dob = Field(attribute='header__cid__dob', column_name='child_birthdate')
    cid_grade = Field(attribute='header__cid__grade', column_name='child_grade')
    cid_genre = Field(attribute='header__cid__genre', column_name='child_sex')
    cid_laterality = Field(attribute='header__cid__laterality', column_name='child_laterality')
    cid_videogames_usage = Field(attribute='header__cid__videogames_usage', column_name='child_videogames_usage')
    cid_diagnostic = Field(attribute='header__cid__diagnostic', column_name='child_learning_disabilities')
    cid_failed_grades = Field(attribute='header__cid__failed_grades', column_name='child_failed_grades')
    cid_school_name = Field(attribute='header__cid__school__name', column_name='school_name')
    cid_school_type = Field(attribute='header__cid__school__type', column_name='school_public_private')
    cid_school_city = Field(attribute='header__cid__school__city', column_name='school_city')
    cid_school_mixed_differetiated = Field(attribute='header__cid__school__mixed_differetiated', column_name='school_mixed_differentiated')
    cid_school_regular_special = Field(attribute='header__cid__school__regular_special', column_name='school_regular_special')
    header_date = Field(attribute='header__date', column_name='session_date')

    class Meta:
        export_order = (
            'parent_email',
            'parent_firstname',
            'parent_lastname',
            'parent_country',
            'cid_id',
            'cid_firstname',
            'cid_lastname',
            'cid_dob',
            'cid_grade',
            'cid_genre',
            'cid_laterality',
            'cid_videogames_usage',
            'cid_diagnostic',
            'cid_failed_grades',
            'cid_school_name',
            'cid_school_type',
            'cid_school_mixed_differetiated',
            'cid_school_regular_special',
            'cid_school_city',
            'header_date',   
        )


class HeaderGamesLimitedResource(resources.Resource):
    parent_country = Field(attribute='header__cid__user__country', column_name='admin_country')
    cid_id = Field(attribute='header__cid__id', column_name='child_id')
    cid_dob = Field(attribute='header__cid__dob', column_name='child_birthdate')
    cid_grade = Field(attribute='header__cid__grade', column_name='child_grade')
    cid_genre = Field(attribute='header__cid__genre', column_name='child_sex')
    cid_laterality = Field(attribute='header__cid__laterality', column_name='child_laterality')
    cid_videogames_usage = Field(attribute='header__cid__videogames_usage', column_name='child_videogames_usage')
    cid_diagnostic = Field(attribute='header__cid__diagnostic', column_name='child_learning_disabilities')
    cid_failed_grades = Field(attribute='header__cid__failed_grades', column_name='child_failed_grades')
    cid_school_type = Field(attribute='header__cid__school__type', column_name='school_public_private')
    cid_school_city = Field(attribute='header__cid__school__city', column_name='school_city')
    cid_school_mixed_differetiated = Field(attribute='header__cid__school__mixed_differetiated', column_name='school_mixed_differentiated')
    cid_school_regular_special = Field(attribute='header__cid__school__regular_special', column_name='school_regular_special')
    header_date = Field(attribute='header__date', column_name='session_date')

    class Meta:
        export_order = (
            'parent_country',
            'cid_id',
            'cid_dob',
            'cid_grade',
            'cid_genre',
            'cid_laterality',
            'cid_videogames_usage',
            'cid_diagnostic',
            'cid_failed_grades',
            'cid_school_type',
            'cid_school_mixed_differetiated',
            'cid_school_regular_special',
            'cid_school_city',
            'header_date',
        )


class FormatFieldsGame(resources.Resource):
    class Meta:
        model = Prueba

    def dehydrate_cid_laterality(self, prueba):
        value = prueba.header.cid.laterality
        laterality = changue_laterality_to_english(value)
        return laterality
    
    def dehydrate_cid_genre(self, prueba):
        value = prueba.header.cid.genre
        genre = changue_genre_to_english(value)
        return genre

    def dehydrate_cid_grade(self, prueba):
        value = prueba.header.cid.grade
        grade = changue_grade_to_english(value)
        return grade


class ArbolMusicalFullResource(resources.ModelResource, HeaderGamesFullResource, FormatFieldsGame):

    class Meta:
        model = ArbolMusicalV2


class ArbolMusicalLimitedResource(resources.ModelResource,
                                  HeaderGamesLimitedResource, FormatFieldsGame):

    class Meta:
        model = ArbolMusicalV2


class ArenaMagicaFullResource(resources.ModelResource, HeaderGamesFullResource, FormatFieldsGame):

    class Meta:
        model = ArenaMagicaV2


class ArenaMagicaLimitedResource(resources.ModelResource,
                                 HeaderGamesLimitedResource, FormatFieldsGame):

    class Meta:
        model = ArenaMagicaV2


class DondeQuedoLaBolitaFullResource(resources.ModelResource,
                                     HeaderGamesFullResource, FormatFieldsGame):

    class Meta:
        model = DondeQuedoLaBolitaV2


class DondeQuedoLaBolitaLimitedResource(resources.ModelResource,
                                        HeaderGamesLimitedResource, FormatFieldsGame):

    class Meta:
        model = DondeQuedoLaBolitaV2


class RioFullResource(resources.ModelResource, HeaderGamesFullResource, FormatFieldsGame):

    class Meta:
        model = RioV2


class RioLimitedResource(resources.ModelResource,
                         HeaderGamesLimitedResource, FormatFieldsGame):

    class Meta:
        model = RioV2


class RecoleccionTesoroFullResource(resources.ModelResource,
                                    HeaderGamesFullResource, FormatFieldsGame):

    class Meta:
        model = RecoleccionTesoroV2


class RecoleccionTesoroLimitedResource(resources.ModelResource,
                                       HeaderGamesLimitedResource, FormatFieldsGame):

    class Meta:
        model = RecoleccionTesoroV2


class SombrasFullResource(resources.ModelResource, HeaderGamesFullResource, FormatFieldsGame):

    class Meta:
        model = SombrasV2


class SombrasLimitedResource(resources.ModelResource,
                             HeaderGamesLimitedResource, FormatFieldsGame):

    class Meta:
        model = SombrasV2


class ChildrenTowiIsalndResource(resources.ModelResource):
    class Meta:
        model = ChildrenTowiIsland


class AverageResource(resources.ModelResource):
    class Meta:
        model = Average


class QuartileResource(resources.ModelResource):
    class Meta:
        model = Quartile
