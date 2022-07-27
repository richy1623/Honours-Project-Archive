#!/usr/bin/perl
#
# Link to config in main bin, and utility routines
# Hussein Suleman
# 8 December 2020

# yank in standard configuraton information
use FindBin;
$cwd = $FindBin::Bin;
do "$cwd/../../data/config/config.pl";

use MIME::Lite;
use Email::Send::SMTP::Gmail;

# get new unique ID
sub getID
{
   my ($domain) = @_;

   my $counter = 1;
   if (-e $counterDir.'/'.$domain.".counter")
   {
      open (my $cfile, $counterDir.'/'.$domain.".counter");
      $counter = <$cfile>;
      chomp $counter;
      close ($cfile);
   }
   $counter++;
   open (my $cfile, '>'.$counterDir.'/'.$domain.".counter");
   print $cfile $counter."\n";
   close ($cfile);
   $counter;
}

# send email
sub sendEmail
{
    my ($useremail, $subject, $message) = @_;
   
	my ($mail,$error)=Email::Send::SMTP::Gmail->new( -smtp=>'smtp.gmail.com',
                                                 -login=>'newhonoursarchive@gmail.com',
                                                 -pass=>'pnwuuewsvnmybvgd');
 
	print "session error: $error" unless ($mail!=-1);
	 
	$mail->send(-to=>$useremail, -subject=>$subject, -body=>$message,
		        -attachments=>'full_path_to_file');
	 
	$mail->bye;
}

# send admins email
sub sendAdminEmail 
{
   my ($subject, $message) = @_;

   foreach my $adminID (@administrators)
   {
      if (-e $userDir.'/'.$adminID.".email.xml")
      {
         my $email = '';
         open (my $efile, $userDir.'/'.$adminID.".email.xml");
         $email = <$efile>;
         chomp $email;
         close ($efile);
       
         if ($email =~ /\<email\>(.*)\<\/email\>/)
         {
            sendEmail ($1, $subject, $message);
         }
      }
   }
}
#sendEmail('newhonoursarchive+1@gmail.com', 'subject', 'body')
