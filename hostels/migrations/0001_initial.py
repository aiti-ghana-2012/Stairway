# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Institution'
        db.create_table('hostels_institution', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('institution_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('location', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('hostels', ['Institution'])

        # Adding model 'Hostel'
        db.create_table('hostels_hostel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hostel_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('hostel_description', self.gf('django.db.models.fields.TextField')()),
            ('manager', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('hostel_manager_details', self.gf('django.db.models.fields.TextField')()),
            ('institution', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hostels.Institution'])),
        ))
        db.send_create_signal('hostels', ['Hostel'])

        # Adding model 'Student'
        db.create_table('hostels_student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('id_number', self.gf('django.db.models.fields.IntegerField')()),
            ('phone_number', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hostels.Institution'])),
            ('program_of_study', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('hostels', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hostels.Hostel'])),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('hostels', ['Student'])

        # Adding model 'Amenities'
        db.create_table('hostels_amenities', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('hostels', ['Amenities'])

        # Adding model 'Rooms'
        db.create_table('hostels_rooms', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('room_number', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('occupancy', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('space_available', self.gf('django.db.models.fields.IntegerField')()),
            ('hostel', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hostels.Hostel'])),
            ('fee', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
        ))
        db.send_create_signal('hostels', ['Rooms'])

        # Adding M2M table for field amenities on 'Rooms'
        db.create_table('hostels_rooms_amenities', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('rooms', models.ForeignKey(orm['hostels.rooms'], null=False)),
            ('amenities', models.ForeignKey(orm['hostels.amenities'], null=False))
        ))
        db.create_unique('hostels_rooms_amenities', ['rooms_id', 'amenities_id'])

        # Adding model 'Reservation'
        db.create_table('hostels_reservation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hostels', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hostels.Hostel'])),
            ('occupancy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['hostels.Rooms'])),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('date_of_registration', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('hostels', ['Reservation'])

        # Adding M2M table for field students on 'Reservation'
        db.create_table('hostels_reservation_students', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('reservation', models.ForeignKey(orm['hostels.reservation'], null=False)),
            ('student', models.ForeignKey(orm['hostels.student'], null=False))
        ))
        db.create_unique('hostels_reservation_students', ['reservation_id', 'student_id'])


    def backwards(self, orm):
        
        # Deleting model 'Institution'
        db.delete_table('hostels_institution')

        # Deleting model 'Hostel'
        db.delete_table('hostels_hostel')

        # Deleting model 'Student'
        db.delete_table('hostels_student')

        # Deleting model 'Amenities'
        db.delete_table('hostels_amenities')

        # Deleting model 'Rooms'
        db.delete_table('hostels_rooms')

        # Removing M2M table for field amenities on 'Rooms'
        db.delete_table('hostels_rooms_amenities')

        # Deleting model 'Reservation'
        db.delete_table('hostels_reservation')

        # Removing M2M table for field students on 'Reservation'
        db.delete_table('hostels_reservation_students')


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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 30, 23, 9, 3, 444320)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 30, 23, 9, 3, 444181)'}),
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
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['hostels.Institution']"})
        }
    }

    complete_apps = ['hostels']
