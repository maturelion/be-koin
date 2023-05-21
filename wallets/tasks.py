import decimal
from celery import shared_task
from earnings.models import EquipmentEarning
from equipments.models import Equipments
from histories.models import Histories
from notifications.models import Notification
from payments.models import Payment
from referrals.models import Referral
from users.models import User
from wallets.models import Wallet
import datetime


now = datetime.datetime.now()


@shared_task
def daily_machine_earning():
    equipped_users = User.objects.filter(has_machine=True)
    for equipped_user in equipped_users:
        wallet = Wallet.objects.get(user=equipped_user)
        user_machines = Equipments.objects.filter(user=equipped_user)
        for user_machine in user_machines:
            referral = Referral.objects.get(user=equipped_user)
            owners_profit = user_machine.machine.daily_profit * user_machine.quantity
            wallet.balance += decimal.Decimal(owners_profit)
            wallet.save()
            equipment_earning, created = EquipmentEarning.objects.get_or_create(user=equipped_user)
            equipment_earning.amount_earned += decimal.Decimal(owners_profit)
            equipment_earning.save()
            Payment.objects.get_or_create(user=equipped_user)
            Histories.objects.create(user=equipped_user, subject=user_machine.machine.name, tx_type="transaction", amount=decimal.Decimal(owners_profit), message="added to balance")
            Notification.objects.create(user=equipped_user, notification_type="transaction", subject=user_machine.machine.name, message=f"+{owners_profit} TRX added to balance")
            if referral.parent and referral.parent.has_machine:
                parent_profit = (user_machine.machine.daily_profit * user_machine.quantity) * 7 / 100
                parent_wallet = Wallet.objects.get(user=referral.parent)
                parent_wallet.balance += decimal.Decimal(parent_profit)
                parent_wallet.save()
                equipment_earning, created = EquipmentEarning.objects.get_or_create(user=referral.parent)
                equipment_earning.amount_earned += decimal.Decimal(owners_profit)
                equipment_earning.save()
                Histories.objects.create(user=referral.parent, subject=user_machine.machine.name, tx_type="transaction", amount=decimal.Decimal(parent_profit), message="added to balance")
                Notification.objects.create(user=referral.parent, notification_type="transaction", subject=user_machine.machine.name, message=f"+{parent_profit} TRX added to balance")
            
            if referral.grand_parent and referral.grand_parent.has_machine:
                grand_parent_profit = (user_machine.machine.daily_profit * user_machine.quantity) * 5 / 100
                grand_parent_wallet = Wallet.objects.get(user=referral.grand_parent)
                grand_parent_wallet.balance += decimal.Decimal(grand_parent_profit)
                grand_parent_wallet.save()
                equipment_earning, created = EquipmentEarning.objects.get_or_create(user=referral.grand_parent)
                equipment_earning.amount_earned += decimal.Decimal(grand_parent_profit)
                equipment_earning.save()
                Histories.objects.create(user=referral.grand_parent, subject=user_machine.machine.name, tx_type="transaction", amount=decimal.Decimal(grand_parent_profit), message="added to balance")
                Notification.objects.create(user=referral.grand_parent, notification_type="transaction", subject=user_machine.machine.name, message=f"+{grand_parent_profit} TRX added to balance")
            
            if referral.great_grand_parent and referral.great_grand_parent.has_machine:
                great_grand_parent_profit = (user_machine.machine.daily_profit * user_machine.quantity) * 2 / 100
                great_grand_parent_wallet = Wallet.objects.get(user=referral.great_grand_parent)
                great_grand_parent_wallet.balance += decimal.Decimal(great_grand_parent_profit)
                great_grand_parent_wallet.save()
                equipment_earning, created = EquipmentEarning.objects.get_or_create(user=referral.great_grand_parent)
                equipment_earning.amount_earned += decimal.Decimal(great_grand_parent_profit)
                equipment_earning.save()
                Histories.objects.create(user=referral.great_grand_parent, subject=user_machine.machine.name, tx_type="transaction", amount=decimal.Decimal(great_grand_parent_profit), message="added to balance")
                Notification.objects.create(user=referral.great_grand_parent, notification_type="transaction", subject=user_machine.machine.name, message=f"+{great_grand_parent_profit} TRX added to balance")
        #     print(f"{now} {equipped_user} Daily {user_machine.machine.name} profit added to wallet")
        # print(f"{now} {equipped_user} funded")
    return f"{now} added to all equipped user wallet"

