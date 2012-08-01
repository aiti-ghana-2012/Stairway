# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Student.studuser'
        db.add_column('hostels_student', 'studuser', self.gf('django.db.models.fields.related.OneToOneField')(default=2, to=orm['auth.User'], unique=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Student.studuser'
        db.delete_column('hostels_student', 'studuser_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 31, 16, 33, 12, 550943)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 31, 16, 33, 12, 550805)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'hostels.amenities': {
            'Meta': {'object_name': 'Amenities'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'hostels.hostel': {
            'Meta': {'object_name': 'Hostel'},
            'hostel_description': ('django.db.models.fields.TextField', [], {}),
            'hostel_manager_details': ('django.db.models.fields.TextField', [], {}),
            'hostel_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hostels.Institution']"}),
            'manager': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'hostels.institution': {
            'Meta': {'object_name': 'Institution'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'location': ('django.db.models.fields.TextField', [], {})
        },
        'hostels.reservation': {
            'Meta': {'object_name': 'Reservation'},
            'date_of_registration': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'hostels': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hostels.Hostel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupancy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hostels.Rooms']"}),
            'roomnumber': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'students': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['hostels.Student']", 'symmetrical': 'False'})
        },
        'hostels.rooms': {
            'Meta': {'object_name': 'Rooms'},
            'amenities': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['hostels.Amenities']", 'symmetrical': 'False'}),
            'fee': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'hostel': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hostels.Hostel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupancy': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'room_number': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'space_available': ('django.db.models.fields.IntegerField', [], {})
        },
        'hostels.student': {
            'Meta': {'object_name': 'Student'},
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'hostels': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hostels.Hostel']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_number': ('django.db.models.fields.IntegerField', [], {}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'program_of_study': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hostels.Institution']"}),
            'studuser': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['hostels']
