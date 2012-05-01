%{!?python_site: %define python_site %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(0)")}
# platform-dependent
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary: Generic library for reporting various problems
Name: libreport
Version: 2.0.5
Release: 20%{?dist}
License: GPLv2+
Group: System Environment/Libraries
URL: https://fedorahosted.org/abrt/
Source: https://fedorahosted.org/released/abrt/%{name}-%{version}.tar.gz
Patch0: 0006-support-interactive-plugins-in-GUI-and-CLI.patch
Patch1: 0007-wizard-if-more-than-one-reporter-is-chosen-select-al.patch
Patch2: 0008-added-xml-file-for-Logger-event.patch
Patch3: 0009-report-cli-don-t-crash-when-invalid-analyzer-is-sele.patch
Patch4: 0011-add-python-bindings-for-interactive-plugins.patch
Patch5: 0012-run_event_on_dir-fix-double-free.patch
Patch6: 0015-honor-minimal-rating.patch
Patch7: 0025-added-minimal-rating-entry-to-all-event-xml-files.patch
Patch8: 0026-rhbz-724999-fix-null-in-summary.patch
Patch9: hide_mailx_in_gui.patch
Patch10: rhel6-keyring.patch
Patch11: 0031-added-bugzilla_event.conf-to-enable-Bugzilla-for-all.patch
Patch12: 0032-improved-compatibility-with-anaconda-rhbz-725857.patch
Patch13: 0001-warn-silently-if-keyring-is-not-available-rhbz-72585.patch
Patch14: 0002-don-t-reload-event-configuration-when-dump_dir-chang.patch
Patch15: 0003-wizard-add-configure-event-button-to-wrong-settings-.patch
Patch16: 0004-check-settings-only-for-last-selected-reporter.patch
Patch17: fix_adding_external_files_to_report.patch
Patch18: emptylines_interactive_di.patch
Patch19: 0001-report-cli-sync-man-page-with-actual-switches.patch
Patch20: 0002-compare-problem-data-by-content-of-file-FILENAME_.patch
Patch22: 0004-fix-wrong-casting.patch
Patch24: 0006-reporter-rhtsupport-improve-the-format-of-reported_t.patch
Patch25: 0007-wizard-rename-Configure-Event-Preferences.patch
Patch26: 0008-attach-file-to-bugzilla-ticket.patch
Patch27: 0009-reporter-rhtsupport-add-a-feature-which-attaches-a-f.patch
Patch28: 0010-remove-report_result.c-move-reported_to-related-code.patch
Patch29: 0011-add-report-compat-tool.-Closes-315-bz-725660.patch
Patch30: 0012-fixed-wrapping-in-comment-textview-rhbz-728132.patch
Patch31: anaconda_newt.patch
Patch32: 0001-reporter-rhtsupport-make-c-CONFFILE-to-have-a-defaul.patch
Patch33: 0002-rename-plugins-Bugzilla.conf-plugins-bugzilla.conf.patch
Patch34: 0003-reporter-bugzilla-rhtsupport-make-help-text-more-con.patch
Patch35: 0004-dd_opendir-require-time-file-to-exist-even-in-read-o.patch
Patch36: 0005-reporter-rhtsupport-stop-hardcoding-RHEL-product-ver.patch
Patch37: 0006-reporter-rhtsupport-do-not-hardcode-blacklisting.patch
Patch38: 0007-report-newt-fix-help-text-option-o-is-mandatory.patch
Patch39: 0008-report-newt-fit-reporting-window-to-standard-termina.patch
Patch40: 0001-added-xml-and-event-conf-for-uploader.patch
Patch41: 0001-read-default-CONFFILE-if-no-c-option-is-given.patch
Patch42: 0001-libreport-code-was-moved-to-abrt.git.patch
Patch43: 0002-libreport-fix-d-delete-option.patch
Patch44: 0006-use-a-fallback-text-editor-if-xdg-open-fails.patch
Patch45: 0033-report-cli-crash-wo-config-rhbz730942.patch
Patch46: 0001-fix-make-check.patch
Patch47: 0002-rhbz-729686-fix-make-check.patch
Patch48: update-man-pages.patch
Patch49: update-translations.patch
Patch50: 0001-reporter-bugzilla-fix-file-attaching-was-using-strle.patch
Patch51: 0002-wizard-support-shell-glob-patterns-in-.xml-item-sele.patch
Patch52: 0003-reporter-bugzilla-add-b-to-make-it-possible-to-attac.patch
Patch53: 0002-wizard-make-pages-title-translatable-rhbz-734789.patch
Patch54: disable_bugzilla.patch
Patch55: 0001-rhbz-728190-man-pages-contain-suspicious-version-str.patch
Patch56: 0001-reporter-rhtsupport-fixes-to-check-for-hints-before-.patch
Patch57: 0002-abrt_rh_support-mark-a-few-strings-for-translation.patch
Patch58: 0003-added-files-with-translatable-strings-to-POTFILES.in.patch
Patch59: 0004-wizard-make-urls-in-dialogs-clickable.patch
Patch60: 0001-report-cli-r-FAKE-DIR-return-1-instead-of-0.patch
Patch61: hint_send_tarbal.patch
Patch62: hint_as_raw_data.patch
Patch63: new_line_for_hyperlink.patch
Patch64: 0001-Add-i18n-initialization-to-report-tool-and-to-report.patch
BuildRequires: dbus-devel
BuildRequires: gtk2-devel
BuildRequires: curl-devel
BuildRequires: desktop-file-utils
BuildRequires: xmlrpc-c-devel
BuildRequires: python-devel
BuildRequires: gettext
BuildRequires: libxml2-devel
BuildRequires: libtar-devel
BuildRequires: intltool
BuildRequires: libtool
BuildRequires: nss-devel
BuildRequires: texinfo
BuildRequires: asciidoc
BuildRequires: xmlto
BuildRequires: newt-devel
# required for update from old report library, otherwise we obsolete report-gtk
# and all it's plugins, but don't provide the python bindings and the sealert
# end-up with: can't import report.GtkIO
# FIXME: can be removed when F15 will EOLed, needs to stay in rhel6!
Requires: libreport-python = %{version}-%{release}
# similarly, needed in order to update the system which has report-plugin-ftp/scp.
# FIXME: can be removed when F15 will EOLed, needs to stay in rhel6!
Requires: libreport-plugin-reportuploader

# for rhel6
%if 0%{?rhel} >= 6
BuildRequires: gnome-keyring-devel
%else
BuildRequires: libgnome-keyring-devel
%endif

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Libraries providing API for reporting different problems in applications
to different bug targets like Bugzilla, ftp, trac, etc...

%package devel
Summary: Development libraries and headers for libreport
Group: Development/Libraries
Requires: libreport = %{version}-%{release}

%description devel
Development libraries and headers for libreport

%package python
Summary: Python bindings for report-libs
# Is group correct here? -
Group: System Environment/Libraries
Requires: libreport = %{version}-%{release}
Provides: report = 0.18-11
Obsoletes: report < 0.18-11
# in report the rhtsupport is in the main package, so we need to install it too
%if 0%{?rhel} >= 6
Requires: libreport-plugin-rhtsupport
%endif

%description python
Python bindings for report-libs.

%package cli
Summary: %{name}'s command line interface
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}

%description cli
This package contains simple command line tool for working
with problem dump reports

%package newt
Summary: %{name}'s newt interface
Group: User Interface/Desktops
Requires: %{name} = %{version}-%{release}
Provides: report-newt = 0.18-11
Obsoletes: report-newt < 0.18-11

%description newt
This package contains a simple newt application for reporting
bugs

%package gtk
Summary: GTK front-end for libreport
Group: User Interface/Desktops
Requires: libreport = %{version}-%{release}
Provides: report-gtk = 0.18-11
Obsoletes: report-gtk < 0.18-11

%description gtk
Applications for reporting bugs using libreport backend

%package gtk-devel
Summary: Development libraries and headers for libreport
Group: Development/Libraries
Requires: libreport-gtk = %{version}-%{release}

%description gtk-devel
Development libraries and headers for libreport-gtk

%package plugin-kerneloops
Summary: %{name}'s kerneloops reporter plugin
Group: System Environment/Libraries
Requires: curl
Requires: %{name} = %{version}-%{release}

%description plugin-kerneloops
This package contains plugin which sends kernel crash information to specified
server, usually to kerneloops.org.

%package plugin-logger
Summary: %{name}'s logger reporter plugin
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: abrt-plugin-logger < 2.0.4
Provides: report-plugin-localsave = 0.18-11
Obsoletes: report-plugin-localsave < 0.18-11
Provides: report-config-localsave = 0.18-11
Obsoletes: report-config-localsave < 0.18-11

%description plugin-logger
The simple reporter plugin which writes a report to a specified file.

%package plugin-mailx
Summary: %{name}'s mailx reporter plugin
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Requires: mailx
Obsoletes: abrt-plugin-mailx < 2.0.4

%description plugin-mailx
The simple reporter plugin which sends a report via mailx to a specified
email address.

%package plugin-bugzilla
Summary: %{name}'s bugzilla plugin
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: abrt-plugin-bugzilla < 2.0.4
Provides: report-plugin-bugzilla = 0.18-11
Obsoletes: report-plugin-bugzilla < 0.18-11
Provides: report-config-bugzilla-redhat-com = 0.18-11
Obsoletes: report-config-bugzilla-redhat-com < 0.18-11

%description plugin-bugzilla
Plugin to report bugs into the bugzilla.

%package plugin-rhtsupport
Summary: %{name}'s RHTSupport plugin
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: abrt-plugin-rhtsupport < 2.0.4

%description plugin-rhtsupport
Plugin to report bugs into RH support system.

%package plugin-reportuploader
Summary: %{name}'s reportuploader plugin
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}
Obsoletes: abrt-plugin-reportuploader < 2.0.4
Provides: report-plugin-ftp = 0.18-11
Obsoletes: report-plugin-ftp < 0.18-11
Provides: report-config-ftp = 0.18-11
Obsoletes: report-config-ftp < 0.18-11
Provides: report-plugin-scp = 0.18-11
Obsoletes: report-plugin-scp < 0.18-11
Provides: report-config-scp = 0.18-11
Obsoletes: report-config-scp < 0.18-11

%description plugin-reportuploader
Plugin to report bugs into anonymous FTP site associated with ticketing system.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch22 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1 -b .cli-code-moved-to-abrt
%patch43 -p1 -b .cli-fix-d-delete-option
%patch44 -p1 -b .fallback-xdg-open
%patch45 -p1 -b .report-cli-crash-wo-config
%patch46 -p1 -b .update-man-pages
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1 -b .disable_bugzilla
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1

%build
# rhbz#728190 remove pre-generated man pages, remove this line after rebase
rm src/plugins/*.1
mkdir -p m4
#rm libtool
rm ltmain.sh
test -r m4/aclocal.m4 || touch m4/aclocal.m4
aclocal
libtoolize
autoconf
automake --add-missing --force --copy
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
CFLAGS="-fno-strict-aliasing"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT mandir=%{_mandir}
%find_lang %{name}

# remove all .la and .a files
find $RPM_BUILD_ROOT -name '*.la' -or -name '*.a' | xargs rm -f
mkdir -p $RPM_BUILD_ROOT/%{_initrddir}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/events.d/
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/events/

# After everything is installed, remove info dir
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

%clean
rm -rf $RPM_BUILD_ROOT

%post gtk
/sbin/ldconfig
# update icon cache
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%postun gtk
/sbin/ldconfig
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans gtk
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README COPYING
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/events.d/
%dir %{_sysconfdir}/%{name}/events/
%dir %{_sysconfdir}/%{name}/plugins/
%config(noreplace) %{_sysconfdir}/%{name}/report_event.conf
%{_libdir}/libreport.so.*
%{_libdir}/libabrt_dbus.so.*
%{_libdir}/libabrt_web.so.*
%exclude %{_libdir}/libabrt_web.so
%{_bindir}/report
%{_mandir}/man1/report.1.gz
%{_mandir}/man5/report_event.conf.5.gz

%files devel
%defattr(-,root,root,-)
# Public api headers:
%{_includedir}/libreport/client.h
%{_includedir}/libreport/dump_dir.h
%{_includedir}/libreport/event_config.h
%{_includedir}/libreport/problem_data.h
%{_includedir}/libreport/report.h
%{_includedir}/libreport/run_event.h
# Private api headers:
%{_includedir}/libreport/internal_abrt_dbus.h
%{_includedir}/libreport/internal_libreport.h
%{_libdir}/libreport.so
%{_libdir}/libabrt_dbus.so
%{_libdir}/pkgconfig/libreport.pc
%dir %{_includedir}/libreport

%files python
%defattr(-,root,root,-)
%{python_sitearch}/report/*
%{python_sitearch}/reportclient/*

%files cli
%defattr(-,root,root,-)
%{_bindir}/report-cli
%{_mandir}/man1/report-cli.1.gz

%files newt
%defattr(-,root,root,-)
%{_bindir}/report-newt

%files gtk
%defattr(-,root,root,-)
%{_bindir}/report-gtk
%{_libdir}/libreport-gtk.so.*

%files gtk-devel
%defattr(-,root,root,-)
%{_libdir}/libreport-gtk.so
%{_includedir}/libreport/internal_libreport_gtk.h
%{_libdir}/pkgconfig/libreport-gtk.pc

%files plugin-kerneloops
%defattr(-,root,root,-)
%{_sysconfdir}/libreport/events/report_Kerneloops.xml
%{_mandir}/man*/reporter-kerneloops.*
%{_bindir}/reporter-kerneloops

%files plugin-logger
%defattr(-,root,root,-)
%{_sysconfdir}/libreport/events/report_Logger.conf
%{_sysconfdir}/libreport/events/report_Logger.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/print_event.conf
%{_bindir}/reporter-print
%{_mandir}/man*/reporter-print.*

%files plugin-mailx
%defattr(-,root,root,-)
%{_sysconfdir}/libreport/events/report_Mailx.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/mailx_event.conf
%{_mandir}/man*/reporter-mailx.*
%{_bindir}/reporter-mailx

%files plugin-bugzilla
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/libreport/plugins/bugzilla.conf
%{_sysconfdir}/libreport/events/report_Bugzilla.xml
%config(noreplace) %{_sysconfdir}/libreport/events/report_Bugzilla.conf
%config(noreplace) %{_sysconfdir}/libreport/events.d/bugzilla_event.conf
# FIXME: remove with the old gui
%{_mandir}/man1/reporter-bugzilla.1.gz
%{_bindir}/reporter-bugzilla

%files plugin-rhtsupport
%defattr(-,root,root,-)
%{_sysconfdir}/libreport/events/report_RHTSupport.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/rhtsupport_event.conf
%config(noreplace) %{_sysconfdir}/libreport/plugins/rhtsupport.conf
%{_mandir}/man1/reporter-rhtsupport.1.gz
%{_bindir}/reporter-rhtsupport

%files plugin-reportuploader
%defattr(-,root,root,-)
%{_mandir}/man*/reporter-upload.*
%{_bindir}/reporter-upload
%{_sysconfdir}/libreport/events/report_Uploader.xml
%config(noreplace) %{_sysconfdir}/libreport/events.d/uploader_event.conf

%changelog
* Wed Oct 26 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-20
- fixed i18n initialization
- Resolves: #749148

* Wed Oct 26 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-19
- rebuild, some translations were not propagated to xml files
- Resolves: #731037

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-18
- updated translations
- Resolves: #731037

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-17
- minor spec file fix
- Resolves: #743198

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-16
- minor fix to the search kbase
- Resolves: #743198

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-15
- fix the kbase searching rhbz#743198
- updated translation Related: #731037
- Resolves: #743198 #731037

* Tue Oct 25 2011 Jiri Moskovcak <jmoskovc@redhat.com>
- fix the spec file changelog
- Resolves: #742474

* Fri Oct 21 2011 Nikola Pajkovsky <npajkovs@redhat.com>
- abrt-cli uses wrong return codes
- Resolves: #742474

* Wed Oct 19 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-14
- reaply the man pages patch
- Resolves: #728190

* Wed Oct 19 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-13
- bumped release
- Resolves: #731037

* Wed Oct 19 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-12
- updated translation rhbz#731037
- search kbase before creating the ticket rhbz#743198
- Resolves: #731037 #743198

* Tue Oct 18 2011 Nikola Pajkovsky <npajkovs@redhat.com>
- man pages contain suspicious version string
  Resolves: #728190

* Thu Oct 13 2011 Jiri Moskovcak <jmoskovc@redhat.com> - 2.0.5-11
- disabled bugzilla rhbz#739936
- own /etc/libreport/plugins/ rhbz#744782
- removed unused patches to make rpmdiff happy
- updated translation
- Resolves: #739936 #744782

* Wed Sep 21 2011 Jiri Moskovcak <jmoskovc@redhat.com> - 2.0.5-10
- make wizard page titles translatable
- updated transaltion
- Resolves: #734789 #731037

* Wed Aug 31 2011 Jiri Moskovcak <jmoskovc@redhat.com> - 2.0.5-9
- fixed make check rhbz#729686
- fixed attaching anaconda-tb* rhbz#731389
- Resolves: #729686 #731389

* Fri Aug 26 2011 Nikola Pajkovsky <npajkovs@redhat.com> - 2.0.5-8
- Missing man pages of report and report.conf
  Resolves: #729957
- Update translations
  Resolves: #731037

* Thu Aug 25 2011 Denys Vlasenko <dvlasenk@redhat.com> - 2.0.5-7
- Fix report-cli crash if config files are missing.
  Resolves: #730942
- Pull in libreport-plugin-reportuploader on update
  (fixes a problem with "yum update" on RHEL system with old report package.
  Resolves: #732683

* Tue Aug 23 2011 Karel Klíč <kklic@redhat.com> - 2.0.5-6
- Added two patches (libreport-code-was-moved-to-abrt.git,
  libreport-fix-d-delete-option) from upstream making report-cli
  -d/--delete to remove DUMP_DIR after reporting. First patch also
  removes --list and --info and --full options, which were already
  moved to abrt-cli.
  Resolves: #726097
- Added fallback text editor for editing multiline fields in Anaconda
  Resolves: #728479

* Fri Aug 05 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-5
- added the report cmdline tool rhbz#725660
- fixed man pages version rhbz#728190
- fixed text wrapping rhbz#728132
- improved dump_dir detection rhbz#728166
- fixed reporting from Anaconda newt ui rhbz#729566
- added defualt config file for rhtsupport rhbz#729566
- make reporters use default conf when -c is not used rhbz#729986
- Resolves: #725660 #728190 #728132 #728166 #729566 #729986

* Tue Aug 02 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-4
- further improvement in Anaconda compatibility rhbz#727243
- warn silently when keyring is not available rhbz#725858
- Resolves: #727243 #725858

* Thu Jul 28 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-3
- improved compatibility with bugzilla
- enabled bugzilla for libreport reports (analyzer=libreport)
- Resolves: #725857

* Mon Jul 25 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-2
- removed mailx from possible reporter list (still enabled as post-create event)
- added python bindings to libreport client lib
- honor reporters minimal rating
- fixed (null) in bz summary
- Related: #714045

* Mon Jul 18 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.5-1
- move reporter plugins from abrt to libreport
- fixed provides/obsolete to properly obsolete report package
- wizard: make more fields editable
- Related: #697494

* Tue Jul 12 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.4-4
- added the python bindings -> obsoleting report

* Mon Jul 11 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.4-3
- bump release

* Mon Jun 27 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.4-2
- removed Provides/Obsoletes: report-gtk
- Resolves: #715373

* Mon Jun 20 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.4-1
- new upstream release
- cleaned some header files

* Thu Jun 16 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.3-1
- added report-cli
- updated translation

* Wed Jun 01 2011 Jiri Moskovcak <jmoskovc@redhat.com> 2.0.2-1
- initial packaging
